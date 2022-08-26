#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:04:29 2019

@author: ntshembho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f = open('H long run.txt', 'r')

w = []
c = []

for line in f:
    line = line.strip()
    if line != "":
        columns = line.split()
        w.append(float(columns[0]))
        c.append(float(columns[1]))

         
plt.plot(w, c)
plt.xlabel(r'Calibrated Wavelength $\lambda [\AA]$')
plt.ylabel('Counts')