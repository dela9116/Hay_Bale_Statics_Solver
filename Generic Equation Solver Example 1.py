import numpy as np
from scipy.optimize import fsolve
from math import sin, cos, atan2, sqrt, pi

# --------------  put names and values of all known variables here  -------------
c1 = 20; c2 = -2
def equations(guesses):
    # ----------- put the names of the unknown variables here ----------
    x,y = guesses
    return  [
    # ------------ define the equations here -----------
    # given as a list of all the EXPRESSIONS to drive to zero
    # separated by commas.  One expression per line looks nice.
    #
        x**2 + y**2 - c1,  # = 0
        x - y - c2,  # = 0
    # _______ end of the equation list
    ]

#------ put guess values for the unknowns here ----
guesses = [2,0]
#-------  the equations are solved here -----
answer = fsolve(equations, guesses)
#------ put names of the unknown variable here, in the same order as above -----
print("x,y")
print(answer)
