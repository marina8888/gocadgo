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
    Z = np.vectorize(lambda cell: cell.T)(network[slice_index, :, :])
    X, Y = np.meshgrid(np.arange(network.shape[1]), np.arange(network.shape[2]))
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = X.flatten()
    y = Y.flatten()
    z = Z.flatten()

    # Surface and contour plots:
    # surf = ax.plot_surface(x, y, z, cmap="autumn_r", lw=0, rstride=1, cstride=1, label=field)
    # contour = ax.contour(x, y, z, 10, lw=3, colors="k", linestyles="solid", label=field)
    # plt.show()


    # triang = Triangulation(x, y)

    # Create a 2D contour plot with tricontourf
    plt.figure(figsize=(8, 6))
    plt.tricontourf(x, y, z, cmap='viridis')
    contour = plt.tricontourf(x, y, z, cmap='viridis', levels=5)  # You can specify levels or leave it to default

    # Set the range for the colorbar
    cbar = plt.colorbar(contour)  # Create the colorbar for the plot
    cbar.set_label('Temperature (K)')  # Label the colorbar
    contour.set_clim(vmin=250, vmax=450)  # Set the limits of the colorbar
    cbar.set_ticks([250, 300, 350, 400, 450])

    print(x)
    print(y)
    print(z)

    plt.xlabel('X')
    plt.ylabel('Y')

    # Show the contour plot
    plt.show()


def calculate_fields(network, field = 'Q'):
    pass