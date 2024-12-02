import cantera as ct

class Cell:
    def __init__(self, gas_type:str, T:float, P:float, m:float):
        """
        Class repressenting a cell in a heat exchanger.
        Parameters
        ----------
        T_in is cell inlet temperature to cell in Kelvin
        P_in is cell inlet pressure in Pa
        m_in is cell inlet mass flow rate in kg/s
        """
        if gas_type == 'N2' or 'nitrogen':
            self.gas = ct.Nitrogen()
        if gas_type == 'Air' or 'air':
            self.gas = ct.Solution('air.yaml')
        else:
            raise ValueError(f'gas type {gas_type} not supported')

        self.q = None
        self.T = T
        self.P = P
        self.m = m

        self.gas.TP = self.T, self.P
        self._cp = self.gas.cp_mass

    def __repr__(self):
        """
        String representation of the cell.
        Returns
        -------

        """
        return f"Cell(Cp = {self._cp}"


    @property
    def P(self):
        """
        Get the pressure in the cell (Pa)
        Returns
        -------

        """
        return self._x

    @P.setter
    def P(self, value):
        """
        Set the pressure in the cell (Pa)
        Parameters
        ----------
        value: set value
        Returns
        -------

        """
        self._x = value

    @property
    def T(self):
        """
        Get the pressure in the cell (K)
        Returns
        -------

        """
        return self._x

    @P.setter
    def T(self, value):
        """
        Set the temperature in the cell (K)
        Parameters
        ----------
        value

        Returns
        -------

        """
        self._x = value

    @property
    def m(self):
        """
        Get the mass flow rate in kg/s
        Returns
        -------

        """
        return self._x

    @P.setter
    def m(self, value):
        """
        Set the mass flow rate in kg/s
        Parameters
        ----------
        value

        Returns
        -------

        """
        self._x = value

    def get_q(self, T_prev):
        self.gas.TP = self.T, self.P
        self.q = self.m * self.gas.cp_mass * (T - T_prev) # anticipated heat transfer between two connected cells
        return self.q

    def update_fields(self):
        self.T  - T_prev = self.q /  # anticipated heat transfer between two connected cells

    def p_factor(self):
        """

        Returns
        -------

        """
        self.p_factor = (self.P_out - self.P_in) / self.gas.density_mass

