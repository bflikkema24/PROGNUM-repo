#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import cos, sin, tan, cosh, sinh 
# Setup a input variable for the function of which the integral will be calculated.
function = (input("function"))
a = float(input("Enter your lower bound"))
b = float(input("Enter your upper bound"))
# Take a large number of values to approximate the integral.
x = np.random.uniform(a,b,100000)
y = eval (function)
integral = np.mean(y) * (b-a)
print(integral)

