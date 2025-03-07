import matplotlib.pyplot as plt
import numpy as np

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

class InertialWorldLine:
    def __init__(self, cts, v):
        """
           Initialize an InertialWorldLine object.

           Parameters:
           cts (numpy.ndarray): Array of coordinate times.
           v (float): Velocity of the world line. Must be less than or equal to the speed of light.
        """
        if v > C:
            raise ValueError("Velocity cannot exceed the speed of light")
        self.cts = cts
        self.xs = v*cts/C

    def __str__(self):
        """
           Return a string representation of the InertialWorldLine object.

           Returns:
               str: A string that represents the coordinate times and positions of the world line.
        """
        return f"WorldLine(ts={self.cts}, xs={self.xs})"

    def Lotentz_Transform(self, v):
        """
            Apply a Lorentz transformation to the world line.

            The Lorentz transformation is applied to the coordinate times and positions
            of the world line based on the given velocity.

            Parameters:
            v (float): The velocity for the Lorentz transformation.

            Returns:
            None
        """
        gamma = Calculate_Lorentz_Factor(v)
        beta = Calculate_Beta(v)
        cts_old = self.cts
        xs_old = self.xs
        self.cts = gamma * (cts_old - beta * xs_old)
        self.xs = gamma * (xs_old - beta*cts_old)

    def Plot(self):
        """
            Plot the world line on a spacetime diagram.

            This method plots the coordinate times (`cts`) against the positions (`xs`)
            of the world line on a spacetime diagram using Matplotlib.

            Returns:
                None
        """
        plt.plot(self.xs, self.cts)

# Create an array of time coordinates.
cts = np.linspace(0, 3 * C, 100)*C

# Configure plot spines and add dotted lightcone.
plt.plot(cts, cts, linestyle="dotted", color="orange")
plt.plot(-cts, cts, linestyle="dotted", color="orange")
plt.gca().spines['left'].set_position('center')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')
plt.xlim([-3*C, 3*C])
plt.ylim([0, 3*C])

# Create and plot worldline.
worldline = InertialWorldLine(cts, C/2)
worldline.Plot()
worldline.Lotentz_Transform(-0.5*C)
worldline.Plot()
plt.savefig("src/example.png")
plt.show()

