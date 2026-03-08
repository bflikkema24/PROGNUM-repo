#!/usr/bin/env python
# coding: utf-8

# In[22]:


import matplotlib
from matplotlib import pyplot as plt
from scipy.integrate import quad
import numpy as np
def gauss(x, A, x0, sig, z0):
    " This function describes the one dimensional Gaussian function."
    return A*np.exp(-(x-x0)**2/(2*sig**2))+z0
# Set up input variables for all the definitions in the function, except for x.
A = float(input(f" A: "))
x0 = float(input(f" x0: "))
sig = float(input(f" sig: "))
z0 = float(input(f" z0: "))
x = np.linspace(-10,10,200)
# Set up input variables for the bounds of integration.
lower_bound = float(input(f"Lower bound: "))
upper_bound = float(input(f"Upper bound: "))
calculated_integral, error = quad(gauss, lower_bound, upper_bound, args = (A,x0,sig,z0))
print(f" The area under the graph is {calculated_integral}.")
y = gauss(x, A, x0, sig, z0)
plt.plot(x,A*np.exp(-(x-x0)**2/(2*sig**2))+z0 )
plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), label = f"Area: {calculated_integral}")
plt.legend()
print("Attempting to show plot")
plt.show()
print("Plot is shown")


# In[ ]:




