import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib as mlp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



f = open('na 22.tsv', 'r') #input file name

n=0
while n<22:
    head=f.readline()
    n+=1

x=[]
y=[]

for line in f:
    line = line.strip()
    columns = line.split()
    x.append(float(columns[0]))
    y.append(float(columns[1]))




newx=[]
newy=[]


start= input('Start point ')
end= input ('End point ')

for i in range(len(x)):
    if x[i]>start and x[i]<end:
        newx.append(x[i])
        newy.append(y[i])
    i+=1

plt.figure()
plt.plot(newx, newy, '.')

def gauss(x, amp, cen, wid):
    return amp*np.exp(-(x-cen)**2/wid)

xmodel=np.linspace(start,end, 100)

ampi = input('initial guess amp ')
centi = input('initial guess cent ')
widi = input('initial guess wid ')

p0= [ampi,centi,widi]


popt, pcov = curve_fit(gauss, newx, newy, p0=p0)

dymin = (newy-gauss(newx, *popt))/0.01
min_chisq = sum(dymin*dymin)
dof = len(newx) - len(popt)

print "Chi square: ",min_chisq
print "Number of degrees of freedom: ",dof
print "Chi square per degree of freedom: ",min_chisq/dof
print()


yfit = gauss(xmodel, *popt)
plt.plot(xmodel, yfit, '-r')

for i,pmin in enumerate(popt):
    print("%2i %12f +/- %10f"%(i,pmin,np.sqrt(pcov[i,i]*np.sqrt(min_chisq/dof))))

print ()
print 'fit: amp=%5.3f, cen=%5.3f, wid=%5.3f' %tuple(popt)

          
plt.show()
