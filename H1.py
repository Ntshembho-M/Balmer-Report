#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:17:31 2019

@author: ntshembho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f = open('H1.txt', 'r')

w = []
c = []

for line in f:
    line = line.strip()
    if line != "":
        columns = line.split()
        w.append(float(columns[0]) - 23.695)
        c.append(float(columns[1]))
    
plt.plot(w, c, 'ro', label = 'Data')
#plt.xlim(4117, 4127)
#plt.show()

def g(x,A,sig,mu):
    return (A/(sig*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/sig)**2)

A0 = 14000
sig0 = 1
mu0 = 4099 #4123

p0 = [A0, sig0, mu0]

name = ['A', 'sig', 'mu']

tmodel = np.linspace(4090, 4110, 1000)#(4118, 4130, 1000)

ystart = g(tmodel, *p0)

popt, pcov = curve_fit(g, w, c, p0)

dymin = (c - g(w,*popt))     
min_chisq = sum(dymin**2)                   
dof = len(w) - len(popt)

print ('Chi square:', min_chisq)
print ('Number of degrees of freedom:',dof)
print ('Chi square per degree of freedom:',min_chisq/dof, '\n')

print('Fitting parameters with 68% C.I.:')
		
#print("Table", labels)

for i,pmin in enumerate(popt): # enumerate is very useful ! 
	print("%2i %âˆ’10s %12f +/âˆ’ %10f%", (i,name[i] ,pmin,np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))


yfit = g(tmodel,*popt)

plt.plot(tmodel, yfit, label = 'fit')
plt.legend()
plt.xlabel(r'Calibrated Wavelength $\lambda [\AA]$')
plt.ylabel('Counts')

plt.show()  

y_max = max(yfit)/2
d =0
print('yhalf', round(y_max))
#max_x = tmodel[12]
#print('x value', max_x)
#x1 = (np.abs(yfit - y_max)).argmin()
#print('x1', x1)