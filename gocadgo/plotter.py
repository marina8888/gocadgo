import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

def show_fields(network:dict, field = 'T', slice_index = 2):
    """
    Plotting a field across sliced 3D data
    Parameters
    ----------
    network: Network.network object
    field: which field to show

    Returns
    -------
    """
    if field not in network:
        raise KeyError(f"Field '{field}' not found in the network.")
    data = network[field][slice_index, :, :]  # Slice the 3D data along the first axis

    # Generate X and Y grid for the data
    x = np.arange(data.shape[1])
    y = np.arange(data.shape[0])
    X, Y = np.meshgrid(x, y)

    # Flatten X, Y, and Z for Triangulation
    Z = data.flatten()
    X_flat = X.flatten()
    Y_flat = Y.flatten()

    # Create a triangulation object for tricontourf
    triang = Triangulation(X_flat, Y_flat)

    # Create the tricontourf plot
    plt.figure(figsize=(8, 6))
    contour = plt.tricontourf(triang, Z)

    # Add a colorbar
    cbar = plt.colorbar(contour)

    # Add labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Tricontourf Plot for Field: {field}")

    # Show the plot
    plt.show()


def calculate_fields(network, field = 'Q'):
    pass