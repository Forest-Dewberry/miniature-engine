#!/usr/bin/env python

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def fn(x, A, B, C) :
	# Antoine function where x is T_k
	return A - B / (x + C)

# Data
T_c = np.array([-18.5, -9.5, 0.2, 11.8, 23.1, 32.7, 44.4, 52.1, 63.3, 75.5])
P = np.array([3.18, 5.48, 9.45, 16.9, 28.2, 41.9, 66.6, 89.5, 129., 187.])
T_k = T_c + 273.15
lnP = np.log(P)

# Set up the model with xdata as T_k, and ydata as lnP
xdata = T_k
ydata = lnP

# Interactive plotting
plt.ion()

# plot the input
plt.plot(xdata,ydata,'b*',label='data')

# Initial seed guess
#ABCguess = [5, 2000, -100]
ABCguess = [1, 50, -1] # This is about as far away as the guess works

# It's all about setting up and running this
popt,pcov = curve_fit(fn,xdata,ydata,ABCguess)

# Pull the answer and plot it
Aopt,Bopt,Copt = popt
plt.plot(xdata,fn(xdata,Aopt,Bopt,Copt),'r.-',
	label='fit: A=%5.3f, B=%5.3f, C=%5.3f' % tuple(popt))

# another way to form strings
print 'fit: A={:5.3f}, B={:5.3f}, C={:5.3f}'.format(Aopt,Bopt,Copt)

plt.xlabel('T_k')
plt.ylabel('lnP')
plt.legend()
plt.show(block = True)