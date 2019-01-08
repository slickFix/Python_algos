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
    err = sum(err)
    
    return err/len(x)

def stepGradient(m,b,x,y,learning_rate):
    
    grad_m = [ (j-(m*i+b))*(-i) for i,j in zip(x,y)]
    grad_b = [ (j-(m*i+b))*(-b) for i,j in zip(x,y)]
    
    grad_m = 2*sum(grad_m)/len(x)
    grad_b = 2*sum(grad_b)/len(x)
    
    m = m+(learning_rate*grad_m)
    b = b+(learning_rate*grad_b)
    
    return (m,b)

def gradientDescentImplementer(initial_m,initial_b,x,y,learning_rate,iterations = 100000):
    m = initial_m
    b = initial_b
    for i in range(iterations):
        m,b = stepGradient(m,b,x,y,learning_rate)
        
    return (m,b)

slope = 5
intercept = 10

x = np.linspace(10,30,num=100)
y = [slope*i+intercept+(random.uniform(-1,1)*20) for i in x]
plt.scatter(x,y)


computeError(slope,intercept,x,y)
stepGradient(3,9,x,y,0.001)

(m,b) = gradientDescentImplementer(3,9,x,y,0.000001)