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
        """I'm the 'x' property."""
        return self._x

    @P.setter
    def P(self, value):
        self._x = value

    @property
    def T(self):
        """I'm the 'x' property."""
        return self._x

    @P.setter
    def T(self, value):
        self._x = value

    @property
    def m(self):
        """I'm the 'x' property."""
        return self._x

    @P.setter
    def m(self, value):
        self._x = value

    @property
    def p_factor(self):
        """

        Returns
        -------

        """
        self.p_factor = (self.P_out - self.P_in) / self.gas.density_mass

