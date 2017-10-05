#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#system parameters
g=1
l=1
w=0.1
R=0.2

#defining the differential equations
def y1(t,y):
    return y
def y2(t,y):
    return -(g/l)*np.sin(y)+w**2*(R/l)*np.cos(y-w*t)

# setting time step and integration limits
start=0
end=20
numPoints=5000
t=np.linspace(start,end,num=numPoints)
dt = t[1]-t[0]

#setting intial condtions
(phi0,vel0)=(0.2,0)
phi = [phi0]
vel = [vel0]
for step in range(numPoints-1):
    timeNow=step*dt
    vel.append(vel0+ dt*y2(timeNow,phi0))
    phi.append(phi0+dt*y1(timeNow,vel0))
    vel0=vel[step+1]
    phi0=phi[step+1]

plt.plot(t,phi)
plt.show()