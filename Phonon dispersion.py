# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:07:51 2020

@author: E09250
"""

import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-10,10,1000)
# y = 1 - np.tanh(x)
alpha_2 = 2
T = 300
beta = 0.125
T = np.linspace(0,5)
y = -np.tanh(T)+1
#t = np.linspace(0,2,100)
E = np.linspace(100, 0, 100)
#n = np.exp(-beta*E)
nu = -0.5
Tc = 0
M = (T-Tc)**nu
plt.plot(T,M,'ko')
#y = np.exp(-alpha_2)*((alpha_2)^t)*(np.math.factorial(t))**-1
#plt.plot(T,y, color = 'k', linewidth = 2.5)
# c = 0.5
# x = np.linspace(0,np.pi)
# y = np.sin(0.5*x)
# y2 = c*x
# om2 = y**2
# k2 = y2**2
# diff = k2-om2

# y3 = y2-y
# y5 = y-y2
# #y4 = np.sqrt(-y4)

# plt.plot(x,y, color = 'k')
# plt.plot(x,y2, color = '0.75')

# #plt.plot(x,y3)
# plt.plot(x,y3, color = 'r')
# plt.hlines(1,0,3, linestyle='dashed')
# plt.xlim(0,np.pi)
# plt.ylim(0,1.6)
plt.xticks([-0.5],['T$_{c}$',])
plt.yticks([0],['0'])
plt.vlines(-0.5,0,5, linestyle = 'dashed')
# plt.ylabel('Energy ($\omega$)')
# plt.xlabel('Wavevector (k)')
plt.ylim(0,1.2)
plt.ylabel('Effective Mass (au)')
plt.xlabel('T-T$_{c}$')

