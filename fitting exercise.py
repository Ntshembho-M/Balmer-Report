import numpy as np
import matplotlib.pyplot as plt

#x = np.array([10, 60, 90, 160, 200, 240, 300])
#y = np.array([47.5, 48.5, 49.5, 50.5, 51.8, 51.9, 52.8])
#yu = np.array([0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 0.5])

import numpy as np
import matplotlib.pyplot as plt
f = open('R_H data.txt', 'r')

mu = []
sig = []

for line in f:
    line = line.strip()
    if line != "":
        columns = line.split()
        mu.append(float(columns[0])*10**(-10))
        sig.append(float(columns[1])*10**(-10))

n = 2 
m = [6, 5, 4, 3]
i = 0
R = []
print('mu', mu)

for i in range (len(mu)):
    R.append(1/(mu[i]*(1/2**2 - 1/m[i]**2)))
    i = i+1

print('R_H', R)

R_H = np.mean(R)
print('R_H real', R_H)

uR = []

print('sig', sig)

for i in range (len(mu)):
    uR.append(R[i]*(sig[i])/mu[i])
print('uR', uR)


#uR1 = np.sqrt((sum(uR**2)))
#print('uR', uR1)

R1 = 10967758.3 
print(R1)

Real = R1-R_H

print('Real', Real)

plt.plot(mu, R_H-R, '.r', label = r'Calculated $R_H$ value')
plt.errorbar(mu, R_H - R, yerr=uR, fmt='+', color = 'grey')
plt.axhline(0,linestyle='--',color='k',label='Deviations from mean')
#plt.axhline(Real,linestyle='--',color='b',label='Deviations from mean')
#plt.axhline(Real,linestyle='--',color='b',label='Deviations from mean')
plt.legend()
plt.xlabel(r'wavelength [m]')
plt.ylabel(r'Deviation from mean $R_H$ value' )
plt.show()