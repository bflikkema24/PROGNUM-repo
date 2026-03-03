#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m = float(input("The apparent magnitude is "))
M = float(input("The absolute magnitude is "))
d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
D = f"The distance to the star is {d} ly"
print (D)

