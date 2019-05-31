import csv
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Fig5doutput.dat")

numrows = len(data)
numcols = len(data[0])


x = data[:,0]
peri0 = data[:,1]
peri5 = data[:,2]
tjperi = data[:,3]
central = data[:,4]

plt.subplot(4,1,1)		
plt.plot(x,peri0)		#distal peripheral
plt.ylabel('Potential (mV)')
plt.xlabel('Time (ms)')

plt.subplot(4,1,2)
plt.plot(x,peri5)		#350 um from Tjunction
plt.ylabel('Potential (mV)')
plt.xlabel('Time (ms)')

plt.subplot(4,1,3)
plt.plot(x,tjperi)		#100 um from Tjunction
plt.ylabel('Potential (mV)')
plt.xlabel('Time (ms)')

plt.subplot(4,1,4)
plt.plot(x,central)		# central axon
plt.ylabel('Potential (mV)')
plt.xlabel('Time (ms)')

plt.show()
