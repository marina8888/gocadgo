import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

def show_fields(network, field = 'T', slice_index = 2):
    """
    Plotting a field across sliced 3D data
    Parameters
    ----------
    network: Network.network object
    field: which field to show

    Returns
    -------

    """
    #  Slicing:
    Z = np.array([[getattr(network[i, j, slice_index], field) for j in range(network.shape[1])] for i in range(network.shape[0])])
    X, Y = np.meshgrid(np.arange(network.shape[1]), np.arange(network.shape[0]))

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Surface and contour plots
    surf = ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0, rstride=1, cstride=1, label=field)
    contour = ax.contour(X, Y, Z, 10, lw=3, colors="k", linestyles="solid", label=field)
    plt.show()


    # Flatten and triangulation interp on the data:
    x = X.flatten().astype(float)
    y = Y.flatten().astype(float)
    z = Z.flatten().astype(float)
    triang = Triangulation(x, y)

    # Create a 2D contour plot with tricontourf
    plt.figure(figsize=(8, 6))
    plt.tricontourf(triang, z, cmap='viridis')

    # Add a colorbar and labels
    plt.colorbar(label=field)
    plt.title(f'Tricontourf of Slice at z={slice_index}')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Show the contour plot
    plt.show()


def calculate_fields(network, field = 'Q'):
    pass