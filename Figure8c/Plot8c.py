import csv
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Fig8coutput.dat")

numrows = len(data)
numcols = len(data[0])


x = data[:,0]
potential = data[:,1]
ina = data[:,2]
ena = data[:,3]
ik = data[:,4]
ek = data[:,5]

plt.subplot(5,1,1)		
plt.plot(x,potential)		
plt.ylabel('Potential (mV)')
plt.xlabel('Time (ms)')

plt.subplot(5,1,2)
plt.plot(x,ina)		
plt.ylabel('INa (mA/cm2)')
plt.xlabel('Time (ms)')

plt.subplot(5,1,3)
plt.plot(x,ena)		
plt.ylabel('ENa (mV)')
plt.xlabel('Time (ms)')

plt.subplot(5,1,4)
plt.plot(x,ik)		
plt.ylabel('IK (mA/cm2)')
plt.xlabel('Time (ms)')

plt.subplot(5,1,5)
plt.plot(x,ek)		
plt.ylabel('EK (mV)')
plt.xlabel('Time (ms)')


plt.show()
