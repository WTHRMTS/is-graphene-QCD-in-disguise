# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:58:21 2020

@author: E09250
"""

import numpy as np


#import numpy.matmul as mm

sigma_1 = np.array(([0,1],[1,0]))

sigma_2 = np.array(([0,1j],[-1j,0]))

sigma_3 = np.array(([1,0],[0,-1]))

S_plus = 0.5*(sigma_1+1j*sigma_2)

S_minus = 0.5*(sigma_1-1j*sigma_2)

Vertex = sigma_1 + sigma_2 + sigma_3

Vertex_conj = sigma_1 - sigma_2 + sigma_3

sigma_OD = (1/np.sqrt(2))*np.array(([0,1+1j],[1-1j,0]))

sigma_OD_conj = (1/np.sqrt(2))*np.array(([0,1-1j],[1+1j,0]))

Lambda_1 = np.array(([0,1,0],[1,0,0],[0,0,0]))

Lambda_2 = np.array(([0,1j,0],[-1j,0,0],[0,0,0]))

Lambda_3 = np.array(([1,0,0],[0,-1,0],[0,0,0]))

Lambda_4 = np.array(([0,0,1],[0,0,0],[1,0,0]))

Lambda_5 = np.array(([0,0,1j],[0,0,0],[-1j,0,0]))

Lambda_6 = np.array(([0,0,0],[0,0,1],[0,1,0]))

Lambda_7 = np.array(([0,0,0],[0,1j,0],[0,-1j,0]))

Lambda_8 = (1/np.sqrt(3))*np.array(([1,0,0],[0,1,0],[0,-2,0]))

#Comm_12 = np.matmul(Lambda_1,Lambda_2)-np.matmul(Lambda_2,Lambda_1)