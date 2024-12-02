def set_initial(T_in=300, P_in=101325, m_in=0.1, gas_type="N2"):
    """
    A function to set the inputs for the boundary conditions (or at least the default)
    Can take custom values for T_in, P_in, etc.
    Parameters
    ----------
    T_in: initial field and inlet temperature in Kelvin
    P_in: initial field and inlet pressure in Pa
    m_in: mass flow rate for initial field and inlet kg/s
    gas_type: "N2" or "Air"
    Returns
    -------
    """
    return {
        'T': T_in,
        'P': P_in,
        'm': m_in,
        'gas_type': gas_type
    }

def set_boundary(P_out, T_out):
    """
    Set the values across a cell at the inlet boundary.
    Parameters
    ----------
    P_out: previous cell's values of Pa
    T_out: previous cell's values of T

    Returns
    -------

    """
    return {
        'P_out': P_out,
        'T_out': T_out,
    }