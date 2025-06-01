import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting
import argparse
from matplotlib import animation


'''
plotting the target functions in PSO implementation
python functions.py --each   # to plot each function in a separate window
python functions.py --gif   # to generate the gif files
'''



# Define benchmark functions

def function1(x, y):
    """Simple quadratic function with sinusoidal components"""
    return (x - 3.14)**2 + (y - 2.72)**2 + np.sin(3*x + 1.41) + np.sin(4*y - 1.73)

def rastrigin(x, y):
    return 20 + x**2 + y**2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))

def ackley(x, y):
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - \
           np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + \
           np.e + 20

def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def sphere(x, y):
  return x**2 + y**2


# Set up grid
x = np.linspace(-5, 5, 150)  # Increased from 100 to 150 points
y = np.linspace(-5, 5, 150)  # Increased from 100 to 150 points
X, Y = np.meshgrid(x, y)

# Function list and titles
functions = [rastrigin, ackley, himmelblau, sphere, function1]
titles = ['Rastrigin Function', 'Ackley Function', 'Himmelblau Function', 'Sphere Function', 'Simple Quadratic Function']
filenames = ['rastrigin.gif', 'ackley.gif', 'himmelblau.gif', 'sphere.gif', 'simple_quadratic.gif']

# Animation parameters
frames = 60  
elev_start = 30  # Start from 30 degrees
elev_end = 90  # Go up to 90 degrees

def create_gif(func, title, filename):
    Z = func(X, Y)

    fig = plt.figure(figsize=(8, 8))  # Square figure size
    ax = fig.add_subplot(111, projection='3d')
    surf = [ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')]
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    
    # Hide axis ticks and grid
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)

    def update(frame):
        # First 20 frames: slight rotation at fixed elevation
        if frame < 20:
            ax.view_init(elev=elev_start, azim=frame * 2)  # Slower rotation
        # Next 20 frames: increase elevation to top view
        elif frame < 40:
            progress = (frame - 20) / 20
            ax.view_init(elev=elev_start + (elev_end - elev_start) * progress, azim=40)
        # Next 20 frames: decrease elevation to bottom view
        elif frame < 60:
            progress = (frame - 40) / 20
            ax.view_init(elev=elev_end - (elev_end - elev_start) * progress, azim=40)
        # Last 20 frames: return to original position
        #else:
        #    progress = (frame - 60) / 20
        #    ax.view_init(elev=elev_start, azim=120 + (240 - 120) * progress)
        return surf

    ani = animation.FuncAnimation(fig, update, frames=frames, blit=False)
    # Save with higher resolution
    ani.save(filename, writer='pillow', fps=10, dpi=80)  # Increased DPI for better quality
    plt.close()
    print(f"Saved: {filename}")

def plot_functions(show_separate=False, create_gifs=False):
    if create_gifs:
        # Generate and save all gifs
        for func, title, fname in zip(functions, titles, filenames):
            create_gif(func, title, fname)
        return

    if show_separate:
        # Plot each function in a separate window
        for i, (func, title) in enumerate(zip(functions, titles), 1):
            fig = plt.figure(figsize=(8, 8))  # Square figure size
            Z = func(X, Y)
            
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
            ax.set_title(title)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('f(X, Y)')
            
            # Hide axis ticks and grid
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])
            ax.grid(False)
            
            plt.tight_layout()
    else:
        # Original combined plot
        fig = plt.figure(figsize=(16, 18))
        for i, (func, title) in enumerate(zip(functions, titles), 1):
            Z = func(X, Y)
            ax = fig.add_subplot(3, 2, i, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
            ax.set_title(title)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('f(X, Y)')
            
            # Hide axis ticks and grid
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])
            ax.grid(False)
        
        plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot benchmark functions')
    parser.add_argument('--each', action='store_true', help='Show each function in a separate window')
    parser.add_argument('--gif', action='store_true', help='Create animated GIFs for each function')
    args = parser.parse_args()
    
    plot_functions(show_separate=args.each, create_gifs=args.gif)
