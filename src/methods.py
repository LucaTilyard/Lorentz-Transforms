import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

C = 299792458

def Calculate_Lorentz_Factor(v):
    """
        Calculate the Lorentz factor for a given velocity.

        The Lorentz factor is defined as:
            gamma = 1 / sqrt(1 - (v^2 / C^2))

        where:
        - v: velocity (in meters per second)
        - C: speed of light in vacuum (approximately 299,792,458 meters per second)

        Parameters:
        v (float): The velocity for which to calculate the Lorentz factor.

        Returns:
        float: The Lorentz factor for the given velocity.
    """
    return 1 / np.sqrt(1 - (v**2 / C**2))

def Calculate_Beta(v):
    """
        Calculate the beta factor for a given velocity.

        The beta factor is defined as:
            beta = v / C

        where:
        - v: velocity (in meters per second)
        - C: speed of light in vacuum (approximately 299,792,458 meters per second)

        Parameters:
        v (float): The velocity for which to calculate the beta factor.

        Returns:
        float: The beta factor for the given velocity.
    """
    return v / C