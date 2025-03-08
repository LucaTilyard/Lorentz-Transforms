from src.methods import *

C = 299792458

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

class NonInertialWorldLine:

    def __init__(self, cts, function):
        """
            Initialize a NonInertialWorldLine object.

            Parameters:
            cts (numpy.ndarray): Array of coordinate times.
            function (callable): A function that takes an array of coordinate times and returns the corresponding positions.

            Returns:
            None
        """
        if self.cts != 0 and self.xs/self.cts > C:
            raise ValueError("Velocity cannot exceed the speed")
        self.cts = cts
        self.xs = function(cts)
        return 1

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
        return 1

    def Plot(self):
        """
            Plot the world line on a spacetime diagram.

            This method plots the coordinate times (`cts`) against the positions (`xs`)
            of the world line on a spacetime diagram using Matplotlib.

            Returns:
                None
        """
        plt.plot(self.xs, self.cts)
        return 1