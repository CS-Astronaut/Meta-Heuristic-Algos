import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Select the objective function (1 to 4)
function_number = 4


# Define objective functions
def function1(x, y):
    """Simple quadratic function with sinusoidal components"""
    return (x - 3.14)**2 + (y - 2.72)**2 + np.sin(3*x + 1.41) + np.sin(4*y - 1.73)

def function2(x, y):
    """Rastrigin Function"""
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y)

def function3(x, y):
    """Ackley Function"""
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) \
           - np.exp(0.5 * (np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.e + 20

def function4(x, y):
    """Himmelblau Function"""
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Function-specific domain ranges
function_ranges = {
    1: (0, 5),
    2: (-5.12, 5.12),
    3: (-5, 5),
    4: (-6, 6)
}

# Choose the function and its range
if function_number == 1:
    f = function1
elif function_number == 2:
    f = function2
elif function_number == 3:
    f = function3
elif function_number == 4:
    f = function4
else:
    raise ValueError("Function number must be between 1 and 4")

# Get range for plotting and swarm initialization
x_min_range, x_max_range = function_ranges[function_number]
y_min_range, y_max_range = function_ranges[function_number]

# Generate function values over grid
x, y = np.meshgrid(np.linspace(x_min_range, x_max_range, 100), 
                   np.linspace(y_min_range, y_max_range, 100))
z = f(x, y)

# Find approximate global minimum in grid
x_min = x.ravel()[z.argmin()]
y_min = y.ravel()[z.argmin()]

# PSO hyperparameters (customized for each function)
if function_number == 1:
    c1 = c2 = 2.5  # Further increased for stronger attraction
    w = 0.3        # Further reduced for better convergence
    n_particles = 100  # Significantly more particles
    max_velocity = 0.1  # Tighter velocity control
elif function_number == 2:
    c1 = c2 = 1.49445
    w = 0.729
    n_particles = 30
elif function_number == 3:
    c1 = c2 = 1.5
    w = 0.7
    n_particles = 40
else:
    c1 = c2 = 1.2
    w = 0.6
    n_particles = 25

# Initialize particles and velocities
np.random.seed(100)
X = np.random.uniform(x_min_range, x_max_range, (2, n_particles))
V = np.random.randn(2, n_particles) * 0.1

# Initialize personal and global bests
pbest = X.copy()
pbest_obj = f(X[0], X[1])
gbest = pbest[:, pbest_obj.argmin()]
gbest_obj = pbest_obj.min()

def update():
    """Run one iteration of PSO"""
    global V, X, pbest, pbest_obj, gbest, gbest_obj
    
    r1, r2 = np.random.rand(2)
    
    # Update velocities with stronger clamping
    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (gbest.reshape(-1, 1) - X)
    if function_number == 1:
        V = np.clip(V, -max_velocity, max_velocity)
    else:
        V_max = 0.1 * (x_max_range - x_min_range)
        V = np.clip(V, -V_max, V_max)
    
    # Update positions
    X = X + V
    X[0] = np.clip(X[0], x_min_range, x_max_range)
    X[1] = np.clip(X[1], y_min_range, y_max_range)
    
    # Evaluate new positions
    obj = f(X[0], X[1])
    
    # Update personal bests
    better = obj < pbest_obj
    pbest[:, better] = X[:, better]
    pbest_obj[better] = obj[better]
    
    # Update global best
    if obj.min() < gbest_obj:
        gbest = X[:, obj.argmin()]
        gbest_obj = obj.min()

# Set up plot
fig, ax = plt.subplots(figsize=(10, 8))
fig.set_tight_layout(True)

# Plot heatmap of function values
img = ax.imshow(z, extent=[x_min_range, x_max_range, y_min_range, y_max_range], 
               origin='lower', cmap='viridis', alpha=0.5)
fig.colorbar(img, ax=ax)

# Mark approximate global minimum
ax.plot([x_min], [y_min], marker='x', markersize=5, color="white", label='Grid Minimum')

# Contour lines
contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")

# Particle visuals
pbest_plot = ax.scatter(pbest[0], pbest[1], marker='o', color='black', alpha=0.5, label='PBest')
p_plot = ax.scatter(X[0], X[1], marker='o', color='blue', alpha=0.5, label='Particles')
p_arrow = ax.quiver(X[0], X[1], V[0], V[1], color='blue', width=0.005, angles='xy', scale_units='xy', scale=1)
gbest_plot = ax.scatter([gbest[0]], [gbest[1]], marker='*', s=100, color='red', alpha=0.8, label='GBest')

# Set axes and title
ax.set_xlim([x_min_range, x_max_range])
ax.set_ylim([y_min_range, y_max_range])
ax.legend(loc='upper right')

function_names = {
    1: "Simple Quadratic Function",
    2: "Rastrigin Function",
    3: "Ackley Function", 
    4: "Himmelblau Function"
}
ax.set_title(f"PSO Optimization for {function_names[function_number]}")
ax.set_xlabel("x")
ax.set_ylabel("y")

def animate(i):
    """Animation frame update"""
    update()
    ax.set_title(f'Iteration {i:02d} - {function_names[function_number]}')
    pbest_plot.set_offsets(pbest.T)
    p_plot.set_offsets(X.T)
    p_arrow.set_offsets(X.T)
    p_arrow.set_UVC(V[0], V[1])
    gbest_plot.set_offsets(gbest.reshape(1, -1))
    return ax, pbest_plot, p_plot, p_arrow, gbest_plot

# Number of iterations
max_iterations = 100

# Create animation
anim = FuncAnimation(fig, animate, frames=list(range(1, max_iterations+1)), 
                     interval=200, blit=False, repeat=True)

# Save animation
function_name_simple = function_names[function_number].replace(" ", "_").lower()
filename = f"PSO_{function_name_simple}.gif"
anim.save(filename, dpi=120, writer="pillow")

# Print optimization results
print("\nOptimization Results:")
print(f"Function: {function_names[function_number]}")
print("-----------------------------")
print(f"PSO found best at f({gbest[0]:.6f}, {gbest[1]:.6f}) = {gbest_obj:.6f}")

# Known global minima
if function_number == 2:
    print("Exact Rastrigin minimum at f(0, 0) = 0")
elif function_number == 3:
    print("Exact Ackley minimum at f(0, 0) = 0")
elif function_number == 4:
    minima = [
        (3.0, 2.0),
        (-2.805118, 3.131312),
        (-3.779310, -3.283186),
        (3.584428, -1.848126)
    ]
    print("Known global minima for Himmelblau:")
    for i, (x, y) in enumerate(minima):
        print(f"  {i+1}. f({x:.6f}, {y:.6f}) = {f(x, y):.6f}")
