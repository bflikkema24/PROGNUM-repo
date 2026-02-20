#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = [1,2]
for i in range (0,99):
    f = x[-1] + x[-2]
    x.append(f)
print(f"The 100th term of the Fibonacci sequence is {x[99]}")

