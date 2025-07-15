from scipy.optimize import fsolve
import numpy as np
from math import sqrt

#------- calculation of static forces in the Haybale Lifter linkage -----

Fy=2000.0 #in the freebody and equations, DOWN was POSITIVE!!!

# non-moving points 1 and 3
x1, y1 = 0, 0
x3, y3 = 2.35, -0.613

#moving points  2  4  and F
x2, y2 =-2.438,      1.407
x4, y4 = -1.984,      -0.978
xf, yf = -0.290,     -2.252

#------------------ no changes needed after this line ---------------
def equations(guesses):
    M,f1x,f1y,f2x,f2y,f3x,f3y,f4x,f4y = guesses
    return  [ # a List of all the EXPRESSIONS to drive to zero
              # for an n-equation and n-unknown problem

        f1x + f2x,  #forces and moments on link 12
        f1y + f2y,
        M - f2x*(y2-y1) + f2y*(x2-x1),

        f3x + f4x,  #forces and moments on link 34
        f3y + f4y,
        -f4x*(y4-y3) + f4y*(x4-x3),

        -f2x-f4x,  #forces and moments on link 24
        -f2y - f4y - Fy,
        -Fy*(xf-x2) +f4x*(y4-y2) -f4y*(x4-x2)
    ]

answer = fsolve(equations, [0,0,0,0,0,0,0,0,0])
# print(answer)
# print()

M,f1x,f1y,f2x,f2y,f3x,f3y,f4x,f4y = answer
print(" M = ", M)
print(" f1x = ",f1x, " f1y = ", f1y)
print(" f2x = ",f2x, " f2y = ", f2y)
print(" f3x = ",f3x, " f3y = ", f3y)
print(" f4x = ",f4x, " f4y = ", f4y)
print()
print("Sanity check - Sum Fx,  Sum Fy, Sum Moments about Joint 3")

# Now do an important SANITY CHECK - necessary but not sufficient!!!
# Looking at only EXTERNAL forces, check the sum of all external forces
# and the sum moments at JOINT-3.  All three answer should be ZERO
print(-Fy + f1y + f3y)
print(f1x + f3x)
print( M - f1x*(y1-y3) + f1y*(x1-x3) - Fy*(xf-x3) )
print("")

#Warning!!!   Semi-advanced geometry!!

def alignForcesToLink(p1x,p1y,p2x,p2y,fx,fy):
    link = np.array([p2x-p1x, p2y-p1y],dtype=float) #use numpy to use the dot product below
    force = np.array([fx,fy],dtype=float)
    linkperp = np.array([-(p2y-p1y), p2x-p1x]) #rotate 90 degrees ccw
    linkmag = sqrt(link[0]**2 + link[1]**2)
    forcemag = sqrt(fx**2 + fy**2)
    forceAlong = np.dot(force,link)/linkmag #use vector dot product to get the component
    forcePerpendicular = np.dot(force,linkperp)/linkmag #use vector dot product to get the component
    return forceAlong, forcePerpendicular

L12 = sqrt(  (x2-x1)**2   + (y2-y1)**2  )
L34 = sqrt(  (x4-x3)**2   + (y4-y3)**2  )
L13 = sqrt(  (x3-x1)**2   + (y3-y1)**2  )
L14 = sqrt(  (x4-x1)**2   + (y4-y1)**2  )
L24 = sqrt(  (x4-x2)**2   + (y4-y2)**2  )
L4f = sqrt(  (xf-x4)**2   + (yf-y4)**2  )

forceAlong,forcePerpendicular = alignForcesToLink(x1,y1,x2,y2,f2x,f2y) #force 2 on link 12

print(f"force2 aligned with the link12: {forceAlong:.1f} and the force perpendicular is: {forcePerpendicular:.1f}")
print(f"the perpendicular force's moment about point 1 is: {L12*forcePerpendicular:.2f} ")

forceAlong,forcePerpendicular = alignForcesToLink(x3,y3,x4,y4,f4x,f4y) #force 4 on link 34

print(f"force4 aligned with the link34: {forceAlong:.1f} and the force perpendicular is: {forcePerpendicular:.1f}")

print()
print(f"link12 length is: {L12:.2f}")
print(f"link34 length is: {L34:.2f}")
print(f"Distance 1-3 is: {L13:.2f}")
print(f"Distance 3-f is: {L4f:.2f}")
print()
print(f"Distance 1-4 is: {L14:.2f}")
print(f"Distance 2-4 is: {L24:.2f}")

pass










