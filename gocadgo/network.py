import numpy as np
from cell import Cell
from helper import set_boundary
class Network:
    def __init__(self, height:int, width:int, length:int, boundary: dict = None):
        """
        Create a network object representing a heat exchanger.
        Parameters
        ----------
        height: by number of cells
        width: by number of cells
        length: by number of cells
        boundary : starting conditions, set by the set_boundary function
        """
        self.network = self.create_network(height, width, length, boundary)
        self.init_fields(boundary)

        # "timestep-like" iteration:
        for t in range(5):
            self.run_network()


    def create_network(self, height, width, length, boundary):
        grid_size = (height, width, length)
        init_Cell = Cell(**boundary)  # boundary condition stored as dict
        network = np.full(grid_size, init_Cell, dtype=object)
        return network

    def init_fields(self, boundary):
        # set boundary conditions to default if user hasn't specified them:
        if boundary is None:
            boundary = set_boundary()

        # the first row (lengthwise) of the network has predefined properties - TO DO:
        self.network[:, :, 0] = Cell(**boundary)

    def run_network(self):
        """
        Iterate one timestep of the network.
        Returns
        -------
        """
        return self.network
