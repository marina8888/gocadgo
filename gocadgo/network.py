import numpy as np
from cell import Cell
from helper import set_boundary, set_initial
class Network:
    def __init__(self, height:int, width:int, length:int, initial: dict = None, boundary: dict = None):
        """
        Create a network object representing a heat exchanger.
        Parameters
        ----------
        height: by number of cells
        width: by number of cells
        length: by number of cells
        boundary : starting conditions, set by the set_boundary function
        """
        self.network = self.create_network(height, width, length, initial)
        self.init_boundary(initial, boundary)

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

        # Iterate over each i and j, update fields for the second slice, and print values
        for i in range(self.network.shape[0]):
            for j in range(self.network.shape[1]):
                # Update the fields of the second cell (network[i, j, 1])
                # Print values for verification
                print(f' values {i} and j {j} updated')
                print(self.network[i, j, 1].T)  # Print the T value of the second cell
                self.network[i, j, 1].update_fields(T_prev=boundary['T_out'], P_prev=boundary['P_out'])


    def run_network(self):
        """
        Iterate one timestep of the network.
        Returns
        -------
        """
        # for i in range(self.network.shape[0]):  # Iterate over the first dimension
        #     for j in range(self.network.shape[1]):  # Iterate over the second dimension
        #         for k in range(self.network.shape[2]):  # Iterate over the third dimension
        #             cell = self.network[i, j, k]
        #             # Perform your operation on each cell
        #             cell.update_fields()

        return self.network
