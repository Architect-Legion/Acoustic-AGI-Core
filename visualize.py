import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from topology import ResonantSphereKernel

def plot_subconscious_heat(kernel):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Extract coordinates and heat values
    if not kernel.energy_grid:
        print("No latent heat detected. Run a test signal first!")
        return

    coords = list(kernel.energy_grid.keys())
    heats = list(kernel.energy_grid.values())
    
    # Convert spherical to cartesian for plotting
    xs, ys, zs = [], [], []
    for r, theta, phi in coords:
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        xs.append(x)
        ys.append(y)
        zs.append(z)

    # Plot the heat map (scatter plot with color mapped to heat)
    sc = ax.scatter(xs, ys, zs, c=heats, cmap='hot', s=50, alpha=0.8)
    plt.colorbar(sc, label='Latent Heat (Energy Units)')

    # Draw a wireframe sphere to represent the 'Skin'
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_sphere = np.cos(u)*np.sin(v)
    y_sphere = np.sin(u)*np.sin(v)
    z_sphere = np.cos(v)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color="cyan", alpha=0.1)

    ax.set_title("Acoustic-AGI: 3D Latent Heat Map (Subconscious)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

if __name__ == "__main__":
    # Simulate a run to generate data
    from test_run import simulate_first_cry
    import sys
    
    # We need to capture the kernel from the test run
    # (Simplified for the demo: we run a fresh sim)
    from topology import ResonantSphereKernel
    k = ResonantSphereKernel()
    # Manual injection of some 'failed thoughts' for the plot
    for _ in range(5):
        k.fractal_dissipation((0.3, np.random.rand()*3.14, np.random.rand()*6.28), 15.0)
    
    plot_subconscious_heat(k)
