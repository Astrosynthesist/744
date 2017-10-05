#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#system parameters
g=1
l=1
w=0
R=0.2

#setting intial condtions
phi = [0.2]
vel = [0]

#defining the differential equations
def y1(t,y):
    return y
def y2(t,y):
    return (w**2)*(R/l)*np.cos(y-w*t)-(g/l)*np.sin(y)

# setting time step and integration limits
start=0
end=100
numPoints=100000
t=np.linspace(start, end, num=numPoints)
dt= t[1]-t[0]

for step in range(0,numPoints-1): # forward Euler's method
    timeNow=step*dt
    vel.append(vel[step]+ dt*y2(timeNow,phi[step]))
    phi.append(phi[step]+dt*y1(timeNow,vel[step]))
plt.plot(t,phi)
plt.show()
