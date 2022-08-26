import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

f = open('Co 60-1.tsv')

channel = []
counts = []
hold = True

for line in f:
    line = line.strip();
    
    if hold:
    	head = line.split(':\t')
    	if head[0] == 'Calibration Coefficients:Elapsed Real Time':
    		time = float(head[1])
    	 
    if not hold:
        col = line.split()
        channel.append(float(col[0]))
        counts.append(float(col[1]))
        
    if line == 'Channel	Energy	Counts':
        hold = False

counts = np.array(counts)
channel = np.array(channel)
noise = []

for i in range(len(counts)):
	if counts[i] != 0:
		noise.append(np.sqrt(counts[i]))
	else:
		noise.append(0)

noise = np.array(noise)

plt.errorbar(channel,  counts/time,  noise/time, np.zeros(len(channel)), "k.") 
plt.show()