# Ant Colony Optimization (ACO) for TSP

This implementation provides a solution for the Traveling Salesman Problem (TSP) using the Ant Colony Optimization algorithm. The algorithm simulates the behavior of ants finding the shortest path between their colony and food sources.

## Algorithm Overview

The implementation includes:
- Pseudo-Random-Proportional Action Choice Rule for node selection
- Local and global pheromone updates
- Heuristic information based on distance
- Support for symmetric TSP instances

## Features

- Configurable number of ants and iterations
- Adjustable parameters for algorithm fine-tuning
- Pheromone evaporation rate control
- Built-in visualization of progress

## Usage

```python
import numpy as np
from ant_colony_optimization import AntColonyOptimization

# Create a distance matrix for your TSP instance
distances = np.array([
    [0, 20, 30, 40, 50],
    [20, 0, 25, 35, 45],
    [30, 25, 0, 30, 40],
    [40, 35, 30, 0, 35],
    [50, 45, 40, 35, 0]
])

# Initialize ACO solver
aco = AntColonyOptimization(
    distances=distances,
    n_ants=10,          # Number of ants
    n_iterations=20,    # Number of iterations
    decay=0.1,         # Pheromone evaporation rate
    alpha=1,           # Pheromone importance
    beta=2            # Heuristic information importance
)

# Run the optimization
best_path, best_length = aco.run()
```

## Parameters

- `distances`: Matrix of distances between nodes
- `n_ants`: Number of ants in the colony
- `n_iterations`: Maximum number of iterations
- `decay`: Pheromone evaporation rate (ρ)
- `alpha`: Importance of pheromone trail (α)
- `beta`: Importance of heuristic information (β)

## Algorithm Details

1. **Initialization**:
   - Creates initial pheromone trails
   - Calculates heuristic information based on distances

2. **Solution Construction**:
   - Each ant constructs a solution path
   - Uses probability-based node selection
   - Applies local pheromone updates during construction

3. **Pheromone Updates**:
   - Local updates during path construction
   - Global updates using the best found path
   - Implements pheromone evaporation

## Output

The algorithm returns:
- Best path found (list of node indices)
- Length of the best path

## Requirements

- NumPy
- Python 3.6+

## References

- Dorigo, M., & Stützle, T. (2004). Ant Colony Optimization. MIT Press.
- Dorigo, M., Maniezzo, V., & Colorni, A. (1996). Ant system: optimization by a colony of cooperating agents.