#!/usr/bin/env python
# coding: utf-8

# Sessionquiz

# 3.1

# In[48]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]


for M in masses:
# To filter out the masses smaller than that of the Moon.    
    if M > 7.349e+22:
        print(M)
m_slice = slice(6,None,1)
print (masses[m_slice])
avg = (sum(masses[m_slice]))/(len(masses[m_slice]))
print (avg)


# In[ ]:




