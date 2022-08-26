#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:12:31 2019

@author: ntshembho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f = open('HeNe.txt', 'r')

w = []
c = []

for line in f:
    line = line.strip()
    if line != "":
        columns = line.split()
        w.append(float(columns[0]))
        c.append(float(columns[1]))
    
plt.plot(w, c, 'ro', label = 'Data')
plt.xlim(6340, 6360)

    
def g(x,A,sig,mu):
    return (A/(sig*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/sig)**2)

A0 = 40000
sig0 = 5
mu0 = 6350

p0 = [A0, sig0, mu0]

name = ['A', 'sig', 'mu']

tmodel = np.linspace(6345, 6360, 1000)

ystart = g(tmodel, *p0)

popt, pcov = curve_fit(g, w, c, p0)

dymin = (c - g(w,*popt))     
min_chisq = sum(dymin**2)                   
dof = len(w) - len(popt)

print ('Chi square:', min_chisq)
print ('Number of degrees of freedom:',dof)
print ('Chi square per degree of freedom:',min_chisq/dof, '\n')

print('Fitting parameters with 68% C.I.:')
		
print("Table", name)

print("Fitted parameters with 68% C.I.:")

for i,pmin in enumerate(popt): # enumerate is very useful ! 
	print("%2i %âˆ’10s %12f +/âˆ’ %10f%", (i,name[i] ,pmin,np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))
print ()


yfit = g(tmodel,*popt)
plt.xlabel(r'Wavelength $\lambda [\AA]$')
plt.ylabel('Counts')
plt.plot(tmodel, yfit, label = 'fit')
plt.legend()
plt.show()  

d = popt[2]-6328
print('change', d)

print(max(c)/2)