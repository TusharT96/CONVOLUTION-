#!/usr/bin/env python
# coding: utf-8

# # #      --Gaussian Kernel Convolution-- and --Central Difference--
#                         #Code by: TUSHAR TARIHALKAR ; SJSU ID 013592202
#                         #python3
#                         #Date: 04/15/2019
#                         #Purpose:
#                         1. Read input data and compute derivative with central difference kernel (the input data points should be greater than 5, so it can test the convolution implementation scalability).
#                         2. Perform convolution with Gaussian kernel to realize noise removal (low pass filtering) operation.
#                         

# In[6]:


#program for --Gaussian Kernel Convolution-- and --Central Difference--
#Code by: TUSHAR TARIHALKAR ; SJSU ID 013592202
import numpy as np
import math

print("input length: ")
uLen = int(input())
print("sigma input: ")
sigma = int(input())
kLen = 3

a=[] #input
g=[] #guass kernel
x=[-1, 0, 1]
o=[]  #output guassian kernel
c=[]  #output central difference

print("input values: ")
for i in range(uLen):
    a.append(int(input()))
print("Gaussian convolution kernel values: ")
for i in range(kLen):
    g.append(((np.exp(-(x[i]**2)/(2*sigma**2)))/((math.sqrt(2*3.142))*sigma))/2)

lenA = uLen-kLen+1
for i in range(lenA):
    f=0
    h=0
    for j in range (kLen):
        f=g[j]*a[i+j]+f
        h=x[j]*a[i+j]+h
    o.append(f)
    c.append(h)
    
print("Guassain convolution output for noise Removal ")
print(o)
print("Diff output")
print(c)


# In[ ]:




