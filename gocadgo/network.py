import numpy as np
from cell import Cell
from helper import set_boundary, set_initial
class Network:
    def __init__(self, height:int, width:int, length:int, inital: dict = None, boundary: dict = None):
        """
        Create a network object representing a heat exchanger.
        Parameters
        ----------
        height: by number of cells
        width: by number of cells
        length: by number of cells
        boundary : starting conditions, set by the set_boundary function
        """
        self.network = self.create_network(height, width, length, inital)
        self.init_fields(inital, boundary)

        # "timestep-like" iteration:
        for t in range(5):
            self.run_network()


    def create_network(self, height, width, length, inital):
        if inital is None:
            inital = set_initial()
            print("Using default initial conditions")

        grid_size = (height, width, length)
        init_Cell = Cell(**inital)  # input as dict
        network = np.full(grid_size, init_Cell, dtype=object)
        return network

    def init_boundary(self, inital, boundary):
        """
        Let's set up the inital values and inlet conditions for network
        Parameters
        ----------
        inital
        boundary

        Returns
        -------

        """
        if boundary is None:
            boundary = set_boundary()
            print("Using default boundary conditions")


        # the first row (lengthwise) of the network has predefined properties:
        self.network[:, :, 0] = Cell(**boundary)
        self.network[:, :, 1] = Cell(**boundary).update_fields(**inital, m=boundary['m']) # is there a better way to write this?

    def run_network(self):
        """
        Iterate one timestep of the network.
        Returns
        -------
        """
        # start_cell.update_fields(**inital)
        return self.network
