import numpy as np
from cell import Cell, StartCell
class Network:
    def __init__(self, height:int, width:int, length:int):
        """
        Create a network object repressenting a heat exchanger.
        Parameters
        ----------
        height: by number of cells
        width: by number of cells
        length: by number of cells
        """
        # initialise a network containing cell objects:
        self.grid_size = (height, width, length)
        self.network = np.empty(self.grid_size, dtype=Cell)

        print(self.grid_size)
        print(self.network)

        # Access a cell:
        print(f"Cell at (0, 0, 0): {self.network[0, 0, 0]}")
        print(f"Cell at (10, 4, 5): {self.network[6, 4, 5]}")

        # Modify a cell:
        self.network[0, 0, 0].q = 8.0
        self.network[0, 0, 0].pressure_loss = 2.0

        print(f"Modified Cell at (0, 0, 0): {self.network[0, 0, 0]}")