#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#system parameters
g=1
l=1
w=0.1
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
t=[start]
dt = (end - start)/numPoints
for i in range(0,numPoints-1): # forward Euler's method
    timeNow=i*dt
    vel.append(vel[i]+ dt*y2(timeNow,phi[i]))
    phi.append(phi[i]+dt*y1(timeNow,vel[i]))
    t.append(t[i]+dt)

plt.title("Angle of pendulum from vertical")
plt.xlabel("t (seconds)")
plt.ylabel(r'$\phi (rad)$')
plt.minorticks_on()
plt.grid(b=True, which='major', color='black')
plt.grid(b=True, which='minor')

plt.plot(t,phi)
plt.show()
