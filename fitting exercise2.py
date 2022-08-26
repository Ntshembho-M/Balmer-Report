import numpy as np
import matplotlib.pyplot as plt

f = open('R_H data.txt', 'r')

mu = np.zeros(4)
sig = np.zeros(4)
i = 0

for line in f:
    line = line.strip()
    columns = line.split()
    mu[i] = float(columns[0])*10**(-10)
    sig[i] = float(columns[1])*10**(-10)
    i = i + 1

n = 2 
m = np.array([6, 5, 4, 3])

R = []

x = 1/m**2
y = 1/mu
p = (sig/mu)
print('p', p)
yu = (1/mu)*p
print('yu', yu)
R1 = 10967758.3
#x = []
#for i in range(4): 
#    x.append(1/m[i]**2)
    
#y =[]
#for i in range(4):
#    y.append(1/mu[i])
#    
#yu = []
#for i in range(4):
#    yu.append(1/sig[i])

xs2 = sum((x**2)/(yu**2))   
xs = sum(x/(yu**2))
ys2 = sum((y**2)/(yu**2))
ys = sum(y/(yu**2))

u = sum(1/yu**2)*xs2 - (xs)**2

m = (sum(1/yu**2) * sum((x*y)/(yu**2)) - xs*ys) / u
print('m',m)
um = ((sum(1/yu**2))/u)**(1/2)
print('um', um)

c = (xs2*ys - xs*sum((x*y)/(yu**2)))/u
print(c)
uc = (xs2/u)**(1/2)
print(uc)

print('x', x)
print('y', y)
print('yu', yu)

#plt.errorbar(x, y, yerr = yu,  fmt='rs', ecolor='-k', label= 'PHY2004W Data', capsize=2)
#plt.legend()
#plt.show()

plt.plot(x, y, '.m', label = 'Data')
plt.errorbar( x, m*x+c, yerr = yu, label = 'Best fit line')
plt.ylabel(r'$\frac{1}{\lambda} [m^-{1}]$')
plt.xlabel(r'$\frac{1}{m^2}$')
plt.legend()
plt.show()
#plt.xlim(0.5,4) 
 

plt.plot(x, m*x+c - y , '.r')
#plt.subplot(212)
plt.errorbar(x,m*x+c-y,yerr=yu,fmt='+',color='grey', label = 'Data with associated uncertainty')
plt.axhline(0,linestyle='--',color='red',label='Expected deviation of data from fit')
yticks = np.arange(-0.5, 50, 200)
plt.yticks(yticks)
plt.xlabel(r'$\frac{1}{m^2}$')
plt.ylabel(r'Deviation from mean $R_H$ value [$m^-{1}$]' )
#plt.ylim(-5000,5000)
#plt.yticks(ticks = 10)
plt.legend()
plt.show()