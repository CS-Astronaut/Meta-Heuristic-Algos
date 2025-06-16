import numpy as np
from ant_colony_optimization import AntColonyOptimization  

# 10 cities
distance_matrix = np.array([
    [  0,  75, 145,  80, 120, 205, 150,  90, 110, 185],
    [ 75,   0,  90, 125,  65, 150, 175, 120,  55, 105],
    [145,  90,   0, 160, 130,  95, 210, 170, 135,  80],
    [ 80, 125, 160,   0,  70, 185, 105, 140, 165, 220],
    [120,  65, 130,  70,   0, 110, 155, 100,  95, 130],
    [205, 150,  95, 185, 110,   0, 190, 125, 140,  75],
    [150, 175, 210, 105, 155, 190,   0,  85, 180, 225],
    [ 90, 120, 170, 140, 100, 125,  85,   0,  65, 115],
    [110,  55, 135, 165,  95, 140, 180,  65,   0,  85],
    [185, 105,  80, 220, 130,  75, 225, 115,  85,   0]
])

n_ants = 20  # ants countity 
n_iterations = 100  
decay = 0.1  # pheromone decay rate (rho)
alpha = 1  # expotation
beta = 2  # exploration

aco = AntColonyOptimization(
    distances=distance_matrix,
    n_ants=n_ants,
    n_iterations=n_iterations,
    decay=decay,
    alpha=alpha,
    beta=beta
)

best_path, best_path_length = aco.run()

print("\nبهترین مسیر پیدا شده:", best_path)
print("طول بهترین مسیر:", best_path_length)

print("\nترتیب بازدید شهرها:")
for i, city in enumerate(best_path[:-1]):  
    print(f"شهر {city}", end=" -> " if i < len(best_path) - 2 else "\n")

print(distance_matrix.shape)