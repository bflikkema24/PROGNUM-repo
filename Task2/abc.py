#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = float(input(f" Your value for a is"))
b = float(input(f" Your value for b is"))
c = float(input(f" Your value for c is"))

x1 = (-b + (b**2 - 4 * a * c)**0.5)/ 2 * a
x2 = (-b - (b**2 - 4 * a * c)**0.5)/ 2 * a

D = b**2 - 4 * a * c
if D == 0:
    print(f" There is one solution.")
elif D > 0:
    print(f" There are two solutions.")
else:
    print( f" No solutions could be found.")


# In[ ]:




