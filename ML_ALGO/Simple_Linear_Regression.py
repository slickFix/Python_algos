#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:19:14 2019

@author: siddharth
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

def computeError(m,b,x,y): # OLS
    
    err = [ abs(j-(m*i+b))**2 for i,j in zip(x,y)]
    
    return sum(err)/len(x)

def stepGradient(m,b,x,y,learning_rate):
    
    grad_m = [ (j-(m*i+b))*(-i) for i,j in zip(x,y)]
    grad_b = [ (j-(m*i+b))*(-b) for i,j in zip(x,y)]
    
    grad_m = 2*(sum(grad_m)/len(x))
    grad_b = 2*(sum(grad_b)/len(x))
    
    m = m+(learning_rate*grad_m)
    b = b+(learning_rate*grad_b)
    
    return (m,b)

def gradientDescentImplementer(initial_m,initial_b,x,y,learning_rate,iterations):
    m = initial_m
    b = initial_b
    
    precision_GD = 0.001
    
    initial_error = computeError(m,b,x,y)
    
    print("initial error "+str(initial_error))
    
    iteration = 0 
    
    while iteration<iterations:
        m,b = stepGradient(m,b,x,y,learning_rate)
        
        new_error = computeError(m,b,x,y)
        
        if(iteration%1000==0):
            print("iteration {}: error is : {}".format(iteration,new_error))
        
# =============================================================================
#         if( initial_error-new_error < precision_GD):
#             break
# =============================================================================
        initial_error = new_error        
        iteration+=1
        
    return (m,b)



# =============================================================================
# # Program begins
# =============================================================================

slope = 5  #m
intercept = 10 #b
x_start = 10  #x range
x_stop = 30   #x range
num_points_in_x = 100 

x = np.linspace(x_start,x_stop,num=num_points_in_x)
y = [slope*i+intercept+(random.uniform(-1,1)*20) for i in x]
plt.scatter(x,y)


ideal_error = computeError(slope,intercept,x,y) #calculating error wrt original slope and intercept

random_slope = random.randint(-100,100)
random_intercept = random.randint(-100,100)
number_iterations = 1000000000
learning_rate = 0.001

i=0
while i<100:
    i+=1
    (random_slope,random_intercept) = stepGradient(random_slope,random_intercept,x,y,learning_rate)
    print("m value is :{} and b value is :{}".format(random_slope,random_intercept))

(m,b) = gradientDescentImplementer(random_slope\
        ,random_intercept,x[:],y[:],learning_rate,number_iterations) # values after gradient descent