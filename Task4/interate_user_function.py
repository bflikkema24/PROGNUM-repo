#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import sin, cos, exp, pi
import numpy as np
from scipy.integrate import quad
# Make an input variable that will be used to plug in a function.
function_input = input(f" Your function: ")
a = eval(input(f" Your lower bound is: "))
b = eval(input(f" Your upper bound is: "))

def y(x):
    "This function is for make the quad command able to evaluate the function_input."
    return eval(function_input)
integral_1, error = quad(y, a, b)  
print(integral_1)
# The Monte Carlo integral
function = (input("function"))
c = eval(input("Enter your lower bound"))
d = eval(input("Enter your upper bound"))
# Take a large number of values to approximate the integral.
x = np.random.uniform(c,d,100000)
y = eval (function)
integral = np.mean(y) * (d-c)
print(integral)


# In[ ]:




