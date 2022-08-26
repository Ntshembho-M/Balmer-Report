'''
Python snippet to read .tsv files from USX multi-run, 
and extract spectrum data
T. Hutton, tanya.hutton@uct.ac.za
Dept Physics, University of Cape Town
April 2018 
'''


import numpy as np

# What file prefix did you choose on USX multi-run? (string)
filePrefix = '?'

# How many runs? (integer)
nRuns = ?

# How many channels are in each spectrum? (integer)
nChannels = ?

# what are your lower and upper limits for integration in channels? (integers)
lowerLimit = 0
upperLimit = nChannels



# Set header length, number of lines to skip
headerLen = 22

# Initialise time array, will contain the integrated 
# number of counts between lowerLimit and upperLimit
# for each run
timeArray = np.zeros(nRuns)


# Initialise summed array, will contain the integrated 
# over all time spectra
sumArray = np.zeros(nChannels)


# Loop through each run file

for i in range(1, nRuns):

#   open file 
    fileName = filePrefix + str(i) + '.tsv'
    fileObject = open(fileName, 'r')    

#   initialise countArray for each run file
    countArray = np.zeros(nChannels)    
    
#   loop through file line-by-line    
    for l, line in enumerate(fileObject):
        
        if l >= headerLen:
#           split line and convert number of counts per channel to float
#           populate countArray channel-by-channel            
            part = line.split()
            countArray[l - headerLen] = float(part[1])

#   close run file to release memory
    fileObject.close()    
    
#   sum counts between lowerLimit and upperLimit
#   populate timeArray run-by-run    
    timeArray[i] = sum(countArray[lowerLimit:upperLimit])

#   add run spectrum to sumArray
    sumArray += countArray
    
    print 'fileName: %s\t integrated counts = %.0f' % (fileName, timeArray[i])
        
            
    
    

