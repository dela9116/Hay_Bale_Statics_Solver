import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad
from math import sin, cos, atan2, sqrt, pi


def equations(guesses):
    # ----------- put the names of the unknown variables here ----------
    Vstall, VTO, A, B, Dist = guesses

    # ------------ define the equations here -----------
    # given as a list of all the EXPRESSIONS to drive to zero
    # separated by commas.  One expression per line looks nice.
    #
    return [
        Vstall - np.sqrt(Weight / (1 / 2 * rho * S * CLmax)),  # = 0
        VTO - 1.2 * Vstall,  # = 0
        A - gc * Thrust / Weight,  # = 0
        B - gc / Weight * (1 / 2 * rho * S * CD),  # = 0
        Dist - quad(lambda V: V / (A - B * V ** 2), a=0, b=VTO)[0]  # = 0
    ]
# _______ end of the equation list


# --------------  put names and values of all known variables here  -------------
gc = 32.2;  rho = 0.002377;  CD = 0.0279;
CLmax = 2.4;  Weight = 56000;  S = 1000;
Thrust = 13000
#------ put guess values for the unknowns here ----
guesses = [0,0,0,0,0]
#-------  the equations are solved here -----
answer = fsolve(equations, guesses)
#------ put names of the unknown variable here, in the same order as above -----
print("Vstall,VTO,A,B")
print(answer)

Vstall,VTO,A,B,Dist=answer
dist_integral = lambda V: V / (A - B * V ** 2)
print(quad(dist_integral, a=0, b=VTO))
