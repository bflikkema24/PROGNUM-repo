#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
x = range(
    -5, 6)

catenary = np.cosh(x)
plt.plot(x, catenary, marker = 'o', color = 'red', label = "cosh(x)")
plt.title("Catenary")
plt.xlabel("x")
plt.ylabel("cosh(x)")
plt.grid()
plt.legend()
plt.show()
X = np.arange(-5,6)

