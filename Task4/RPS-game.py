#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
choice = input("Type R, P or S")
options = np.array(['R', 'P', 'S'])
# Letting the computer choose R, P or S
game = np.random.randint(0,len(options))
computer_choice = options[game]
if choice == computer_choice:
    print("The game is tied.")
# Results if you choose R
elif choice == 'R' and computer_choice == 'S':
    print("You win.")
elif choice == 'R' and computer_choice == 'P':
    print("You lose.")
# Results if you choose P
elif choice == 'P' and computer_choice == 'S':
    print("You lose.")
elif choice == 'P' and computer_choice == 'R':
    print("You win.")
# Results if you choose S    
elif choice == 'S' and computer_choice == 'P':
    print("You win.")
elif choice == 'S' and computer_choice == 'R':
    print("You lose")
# Result if you type something other than R, P or S.
else:
    print("Incorrect input")


# In[ ]:




