import cantera as ct

class Cell:
    def __init__(self, T:float, P:float, m:float, gas_type:str):
        """
        Class repressenting a cell in a heat exchanger.
        Parameters
        ----------
        T is cell inlet temperature to cell in Kelvin
        P is cell inlet pressure in Pa
        m is cell inlet mass flow rate in kg/s
        """
        if gas_type == 'N2' or 'nitrogen':
            self.gas = ct.Nitrogen()
        if gas_type == 'Air' or 'air':
            self.gas = ct.Solution('air.yaml')
        else:
            raise ValueError(f'gas type {gas_type} not supported')
        self.q = 0
        self.T = T
        self.P = P
        self.m = m
        self.gas.TP = self._T, self._P


    def __repr__(self):
        """
        String representation of the cell.
        Returns
        -------

        """
        return f"Cell(T = {self.T}, P = {self.P}, m = {self.m})"


    @property
    def P(self):
        """
        Get the pressure in the cell (Pa)
        Returns
        -------

        """
        return self._P

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
        self._P = value

    @property
    def T(self):
        """
        Get the pressure in the cell (K)
        Returns
        -------

        """
        return self._T

    @T.setter
    def T(self, value):
        """
        Set the temperature in the cell (K)
        Parameters
        ----------
        value

        Returns
        -------

        """
        self._T = value

    @property
    def m(self):
        """
        Get the mass flow rate in kg/s
        Returns
        -------

        """
        return self._m

    @m.setter
    def m(self, value):
        """
        Set the mass flow rate in kg/s
        Parameters
        ----------
        value

        Returns
        -------

        """
        self._m = value

    def update_q(self, T_prev:float):
        self.gas.TP = self._T, self._P
        self.q = self._m * self.gas.cp_mass/1000 * (self.T - T_prev) # anticipated heat transfer between two connected cells

    def update_fields(self, T_prev:float, P_prev:float):
        self.update_q(T_prev)
        print(self.q)
        self.T = self.q / (self._m * self.gas.cp_mass/1000) + T_prev # anticipated heat transfer between two connected cells

    def p_factor(self):
        """

        Returns
        -------

        """
        self.p_factor = (self.P_out - self.P_in) / self.gas.density_mass

