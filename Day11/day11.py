# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:01:41 2019

@author: KIIT
"""
import matplotlib.pyplot as plt
# Reshaping an array
import numpy as np
l = list(map(int,input().split()))
x = np.array(l)
x = x.reshape(3,3)
print(x.ndim)
print(x)


# using normal
                            # mean,sd,no.of entries
incomes = np.random.normal(100.0,20.0,10000)
incomes = np.append(incomes,1000000)
mean = np.mean(incomes)
median = np.median(incomes)
plt.hist(incomes,1)
plt.show()

# Create random array
# Most frequent value using numpy
array = np.random.randint(5,15,40)
u,indices = np.unique(array,return_inverse=True)
u[np.argmax(np.bincount(indices))]

# Most frequent value 
from collections import Counter
max1 = 0
freq = Counter(array)
for k,v in freq.items():
    if v>max1:
        max1 = k
print(max1)
k=max(Counter.values(freq))



# Normal distributed 


array = np.random.normal(150,20,1000)
standard_deviation = np.std(array)
variance = np.var(array)
plt.hist(array,100,color='r')
plt.show()