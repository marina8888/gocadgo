import numpy as np
import json
from helper import set_boundary, set_initial, validate_config
import cantera as ct

class Network:
    def __init__(self, path_to_config = 'config.json', k_t=None, k_p=None):
        """
        Create a network object representing a heat exchanger.
        Parameters
        ----------
        dims: list of [width, height, length] dimensions (by an integer number of elements)
        boundary : starting conditions, set by the set_boundary function
        """
        self.config = self.load_config(path_to_config)

        try:
            validate_config(self.config)
        except ValueError as e:
            print(f"Validation error: {e}")

        self.hot_network, self.cold_network = self.create_network()

        if k_t or k_p is None:
            self.k_t = self._get_k_t()
            self.k_p = self._get_k_p()
        else:
            self.k_t, self.k_p = k_t, k_p

        # "timestep-like" iteration:
        for t in range(5):
            self.run_network(self.hot_network)

    def load_config(self, path_to_config):
        with open(path_to_config, 'r') as file:
            config_data = json.load(file)
            print(config_data)
        return config_data

    def create_network(self):
        """
        Instantiate a network with the correct initial conditions
        Returns
        -------

        """
        def create_single_network(name):
            network = {
                key: np.full(self.config["sim"]["dimensions"], self.config[name]["i"][i])
                for i, key in enumerate(self.config["sim"]["key_list"])
            }
            # set initial mass flow rate:
            network['m'] = network['m'] / (self.config["sim"]["dimensions"][0] * self.config["sim"]["dimensions"][1])

            # set initial c_p:
            gas = None
            if self.config[name]["gas_type"] in ["N2", "nitrogen", "Nitrogen"]:
                gas = ct.Nitrogen()
                print(f"{gas} - N2 network creating!")
            elif self.config[name]["gas_type"] in ["air" or "Air"]:
               gas = ct.Solution('air.yaml')
               print(f"{gas} - Air network creating!")
            else:
                raise ValueError(f"Unknown gas type: {network['gas_type']}")

            gas.TP = self.config[name]["i"][0], self.config[name]["i"][1]
            network["c_p"] = np.full(self.config["sim"]["dimensions"], gas.cp_mass) / 1000

            print(f'Created network: {network}')
            return network

        # Create the hot and cold networks
        hot_network = create_single_network("hot")
        cold_network = create_single_network("cold")

        # Adjust 'm' in both networks and get cp of first cell:
        for network in [cold_network, hot_network]:

            return hot_network, cold_network

    def _get_k_t(self):
        """
        Temperature constant for the system is as follows:
        k_t = (T_1(H) - T_0(H)) * m_dot(H) * c_p(H) /((T_0(H) - T_0(C))
        k_t = (T_1(C) - T_0(C)) * m_dot(C) * c_p(C) /((T_0(H) - T_0(C))

        Order of indexing in config sheets must match to "key_list": ["T", "P", "m"]
        Returns
        -------
        """
        # k_t = (self.config["hot"]["s"][0] - self.config["hot"]["i"][0]) * self.config["hot"]["i"][2] * self._cp_i /((T_0(H) - T_0(C))
        # print(f"K_t_1 is {k_t_1}")
        # k_t = (T_1(H) - T_0(H)) * m_dot(H) * c_p(H) /((T_0(H) - T_0(C))
        # print(f"K_t_1 is {k_t_1}")
        k_t = 0.2
        return k_t
    def _get_k_p(self):
        """

        Pressure constant for the system is as follows:
        k_p = (P_1(C) - P_0(C)) / rho_1(C) * m_dot(C)
        k_p = (P_1(H) - P_0(H)) / rho_1(H) * m_dot(H)

        Order of indexing in config sheets must match to "key_list": ["T", "P", "m"]
        Returns
        -------
        """
        # k_p_1 = (T_1(H) - T_0(H)) * m_dot(H) * c_p(H) /((T_0(H) - T_0(C))
        # print(f"K_p_1 is {k_p_1}")
        # k_p_2 = (T_1(H) - T_0(H)) * m_dot(H) * c_p(H) /((T_0(H) - T_0(C))
        # print(f"K_p_2 is {k_p_2}")
        k_p = 0.01
        return k_p

    def _get_T_1(self, T_slice):
        """
        Forward iteration on T for a given slice.

        Parameters
        ----------
        T_slice: 2D array of temperature values at the current z-plane.

        Returns
        -------
        2D array of temperature values for the next z-plane.
        """
        return T_slice + 10  # Example calculation: Increase temperature by 10.

    def run_network(self, network):
        for z in range(1, self.config["sim"]["dimensions"][2]):
            print(network["T"])
            network["T"][:, :, z] = self._get_T_1(network["T"][:, :, z - 1])
            print(network["T"])
            # network.P[:, :, z] = _get_P_1(network.P[:, :, z - 1])
