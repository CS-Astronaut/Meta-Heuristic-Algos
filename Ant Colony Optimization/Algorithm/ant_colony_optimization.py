import numpy as np
import random

class AntColonyOptimization:
    def __init__(self, distances, n_ants, n_iterations, decay, alpha=1, beta=2):
        """
        Initialize ACO algorithm parameters
        
        Args:
            distances: Matrix of distances between nodes
            n_ants: Number of ants in the colony
            n_iterations: Maximum number of iterations
            decay: Pheromone evaporation rate (rho)
            alpha: Importance of pheromone trail
            beta: Importance of heuristic information
        """
        self.distances = distances
        self.n_nodes = distances.shape[0]
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        
        # Initialize pheromone trails
        # Using the formula τ0 = (n / Ln)^-1 where n is number of nodes
        # and Ln is approximate total distance
        approx_distance = np.mean(self.distances) * self.n_nodes
        self.pheromones = np.ones(self.distances.shape) / (self.n_nodes * approx_distance)
        
        # Heuristic information - inverse of distance
        self.heuristic = 1 / (self.distances + 1e-10)  # Add small value to avoid division by zero
    
    def select_next_node(self, ant, current_node, unvisited):
        """
        Select next node using the Pseudo-Random-Proportional Action Choice Rule
        """
        if not unvisited:
            return None
        
        # Calculate probabilities for each unvisited node
        probabilities = []
        denominator = 0
        
        for node in unvisited:
            # Calculate numerator using formula [τ_ij]^α [η_ij]^β
            numerator = (self.pheromones[current_node, node] ** self.alpha) * \
                         (self.heuristic[current_node, node] ** self.beta)
            probabilities.append(numerator)
            denominator += numerator
        
        # Normalize probabilities
        probabilities = np.array(probabilities) / denominator
        
        # Select next node based on calculated probabilities
        selected = random.choices(unvisited, weights=probabilities, k=1)[0]
        return selected
    
    def local_pheromone_update(self, i, j):
        """
        Update pheromone trails locally using formula:
        τij(t) = (1-ρ)·τij(t-1) + ρ·τ0
        """
        # Calculate initial pheromone value τ0
        approx_distance = np.mean(self.distances) * self.n_nodes
        tau_0 = 1 / (self.n_nodes * approx_distance)
        
        # Update pheromone
        self.pheromones[i, j] = (1 - self.decay) * self.pheromones[i, j] + self.decay * tau_0
        self.pheromones[j, i] = self.pheromones[i, j]  # Ensure symmetry
    
    def global_pheromone_update(self, best_path, best_path_length):
        """
        Update pheromone trails globally using formula:
        τij(t) = (1-ρ)·τij(t-1) + ρ·Δτij where Δτij = 1/L+
        """
        # Evaporate pheromone on all edges
        self.pheromones = (1 - self.decay) * self.pheromones
        
        # Add new pheromone to the edges of the best path
        delta_tau = 1.0 / best_path_length
        
        for i in range(len(best_path) - 1):
            self.pheromones[best_path[i], best_path[i+1]] += self.decay * delta_tau
            self.pheromones[best_path[i+1], best_path[i]] = self.pheromones[best_path[i], best_path[i+1]]
    
    def construct_solutions(self):
        """
        Construct solutions for all ants in the colony
        """
        all_paths = []
        all_path_lengths = []
        
        for ant in range(self.n_ants):
            # Start from a random node
            current_node = random.randint(0, self.n_nodes - 1)
            path = [current_node]
            unvisited = list(range(self.n_nodes))
            unvisited.remove(current_node)
            path_length = 0
            
            # Construct the complete path
            while unvisited:
                next_node = self.select_next_node(ant, current_node, unvisited)
                path.append(next_node)
                path_length += self.distances[current_node, next_node]
                
                # Local pheromone update
                self.local_pheromone_update(current_node, next_node)
                
                current_node = next_node
                unvisited.remove(next_node)
            
            # Complete the tour by returning to the starting node
            path.append(path[0])
            path_length += self.distances[path[-2], path[0]]
            
            all_paths.append(path)
            all_path_lengths.append(path_length)
        
        return all_paths, all_path_lengths
    
    def run(self):
        """
        Run the ACO algorithm
        """
        best_path = None
        best_path_length = float('inf')
        
        for iteration in range(self.n_iterations):
            # Construct solutions for all ants
            all_paths, all_path_lengths = self.construct_solutions()
            
            # Find the best path in this iteration
            iteration_best_path_idx = np.argmin(all_path_lengths)
            iteration_best_path = all_paths[iteration_best_path_idx]
            iteration_best_path_length = all_path_lengths[iteration_best_path_idx]
            
            # Update the best path found so far
            if iteration_best_path_length < best_path_length:
                best_path = iteration_best_path
                best_path_length = iteration_best_path_length
            
            # Global pheromone update using the best path
            self.global_pheromone_update(best_path, best_path_length)
            
            print(f"Iteration {iteration + 1}/{self.n_iterations}, Best length: {best_path_length:.2f}")
        
        return best_path, best_path_length


# Example usage for solving TSP
if __name__ == "__main__":
    # Create a sample distance matrix (symmetric)
    n_cities = 5
    np.random.seed(42)
    distances = np.random.randint(10, 100, size=(n_cities, n_cities))
    # Make it symmetric
    distances = (distances + distances.T) / 2
    # Set diagonal to 0
    np.fill_diagonal(distances, 0)
    
    print("Distance Matrix:")
    print(distances)
    
    # Create and run ACO
    aco = AntColonyOptimization(
        distances=distances,
        n_ants=10,
        n_iterations=20,
        decay=0.1,
        alpha=1,
        beta=2
    )
    
    best_path, best_path_length = aco.run()
    
    print("\nBest path found:", best_path)
    print("Best path length:", best_path_length)