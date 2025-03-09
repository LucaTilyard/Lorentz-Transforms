from src.methods import *
from src.worldLines import *
import numpy as np
import matplotlib.pyplot as plt

C = 299792458

cts = np.linspace(0, 3, 100)*C

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

# Define function for worldline
def Function(cts):
    return(1/C * cts **2)

worldline = NonInertialWorldLine(cts, Function)
worldline.Plot()

#plt.savefig("src/example.png")
plt.show()

print(np.diff(np.diff(cts)/np.diff(Function(cts))))