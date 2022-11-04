# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:33:00 2022

@author: goliakovea
"""
#from mpl_toolkits import mplot3d
import numpy as np
#from scipy.optimize import fsolve
import math
import matplotlib.pyplot as plt

GA = 1
GB = 1

def jacks_mor_n_sw(K, Ga, Gb):
    return (Ga*Gb/4) * ((math.pi/K)**2) + ((Ga + Gb)/2) * \
           (1 - ((math.pi/K)/(math.tan(math.pi/K)))) + \
           2*math.tan(math.pi/(2*K))/(math.pi/(2*K)) - 1

K0n_sw = 0.5
K0_sw = 1

while jacks_mor_n_sw(K0n_sw, GA, GB) > 0:
    K0n_sw += 0.0001
    
print('Коэффициент расчетной длины для несвободных рам: ', round(K0n_sw, ndigits=2))

def jacks_mor_sw(K, Ga, Gb):
    if Ga == 0 and Gb == 0:
        return 0
    else:
        return ((Ga*Gb*(math.pi/K)**2 - 36)/(6*(Ga + Gb))) - \
               ((math.pi/K)/(math.tan(math.pi/K)))

while jacks_mor_sw(K0_sw, GA, GB) > 0:
    K0_sw += 0.0001

print('Коэффициент расчетной длины для свободных рам: ', round(K0_sw, ndigits=2))
        
'''k = np.linspace(5001, 9999, 10000)
x = []

for i in k:
    x.append(jacks_mor_n_sw(i/10000, GA, GB))

plt.subplot(2, 1, 1)    
plt.plot(k/10000, x)
plt.xlabel('K')
plt.ylabel('JMfunc')
plt.title('Non-Sway Frames', loc='right')

plt.grid()

k = np.linspace(10001, 100000, 10000)
x = []

for i in k:
    x.append(jacks_mor_sw(i/10000, GA, GB))

plt.subplot(2, 1, 2)    
plt.plot(k/10000, x, 'r')
plt.xlabel('K')
plt.ylabel('JMfunc')
plt.title('Sway Frames', loc='right')

plt.grid()'''

x = np.linspace(0, 15, 40)
y = np.linspace(0, 15, 40)

xgrid, ygrid = np.meshgrid(x, y)

z = np.zeros((40, 40))
cnt1 = -1
cnt2 = 0

for i in xgrid:
    cnt1 += 1
    cnt2 = 0
    for j in ygrid:
        K0_sw = 1
        while jacks_mor_sw(K0_sw, i[cnt1], j[cnt2]) > 0:
            K0_sw += 0.0001
        z[cnt1, cnt2] = (K0_sw)
        cnt2 += 1

fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')
ax_3d.plot_surface(xgrid, ygrid, z, cmap='jet')
plt.title('Length Cefficients ''K'' For Sway Frames')
plt.xlabel('GA')
plt.ylabel('GB')
