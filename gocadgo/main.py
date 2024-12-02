from gocadgo.network import Network
from gocadgo.cell import Cell
from helper import set_boundary, set_initial
from plotter import show_fields

def main():
    HEIGHT = 40
    WIDTH = 10
    LENGTH = 20

    # setting up inital field:

    air_init = set_initial(T_in=20,
                 P_in=100000,
                 m_in=0.034/(HEIGHT*WIDTH),
                 gas_type="air"
                 )

    nitrogen_init = set_initial(T_in=350,
                 P_in=440000,
                 m_in=0.01/(HEIGHT*WIDTH),
                 gas_type="N2"
                 )

    air_boundary = set_boundary(T_out=30, P_out=99985)
    nitrogen_boundary = set_boundary(T_in=300, P_in=439995)

    # create mesh and run network:
    air_train = Network(WIDTH, HEIGHT, LENGTH, air_init, air_boundary)
    nitrogen_train = Network(WIDTH, HEIGHT, LENGTH, nitrogen_init, nitrogen_boundary)

    # display fields of interest:
    show_fields(air_train.network, 'T')

if __name__ == "__main__":
    main()
