def darcys_law(k, mu, delta_p, length, area):
    """
    Calculates the flow rate based on Darcy's Law.

    Parameters:
    k (float): Permeability of the rock (in Darcies or m^2)
    mu (float): Dynamic viscosity of the fluid (in Pa.s)
    delta_p (float): Pressure difference (in Pa)
    length (float): Length over which the pressure difference is measured (in m)
    area (float): Cross-sectional area through which fluid flows (in m^2)

    Returns:
    float: Flow rate (in m^3/s)
    """
    grad_p = delta_p / length  # Calculating pressure gradient
    flow_rate = (k / mu) * grad_p * area
    return flow_rate

# Example values
permeability = 1.5e-12  # Permeability in m^2 (example value)
viscosity = 1e-3       # Viscosity in Pa.s (example value)
pressure_difference = 500  # Pressure difference in Pascals (example value)
flow_length = 10       # Length in meters (example value)
cross_sectional_area = 0.05  # Area in square meters (example value)

# Calculate the flow rate
flow_rate = darcys_law(permeability, viscosity, pressure_difference, flow_length, cross_sectional_area)

print(f"Flow rate: {flow_rate} m^3/s")



