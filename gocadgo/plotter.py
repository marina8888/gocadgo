import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def show_fields(network, field = 'T'):

    Z = np.array([[getattr(network[i, j, 0], field) for j in range(network.shape[1])] for i in range(network.shape[0])])
    X, Y = np.meshgrid(np.arange(network.shape[1]), np.arange(network.shape[0]))

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0, rstride=1, cstride=1)
    contour = ax.contour(X, Y, Z, 10, lw=3, colors="k", linestyles="solid")
    plt.show()