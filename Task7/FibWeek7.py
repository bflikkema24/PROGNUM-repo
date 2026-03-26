#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self, N, M):          # Initialising the class
        self.N = N
        self.M = M
    def fib1(self):                    # Function for the regular Fibonacci sequence
        sequence = [0,1]
        for n in range (2, 1000):
            sequence.append(sequence[-1] + sequence[-2])
        return f" The {self.N}nth term of the sequence is {sequence[self.N]}"
    def fib2(self):                   # Function for the Fibonacci sequence with the
        sequence1 = [0,1]
        sequence2 = []
        while len(sequence1) < self.N:
            if sequence1[-1] % self.M == 0:
                sequence2.append(sequence1[-1])
            sequence1.append(sequence1[-1] + sequence1[-2])
            if self.N > 0 and 0% self.M == 0:
                    sequence2.insert(0,0)
        return sequence2
        
# Ask for values of N and M        
N = int(input("Your value for N is: "))
M = int(input("Your value for M is: "))           
seq = Fibonacci(N,M)
first_fib = seq.fib1()
print(first_fib)
second_fib = seq.fib2()
print(second_fib)

