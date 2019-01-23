#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:51:03 2019

@author: siddharth
"""

import numpy as np

def InsertionSort_rec(li,k):
    
    if k>1:
        InsertionSort_rec(li,k-1)
        li[:k] = isort(li[:k],k)# using "li[:k] =" as li and li_i don't share memory


def isort(li_i,k):
    
    # list li_i memory is different than the li as it's a slice of li
    pos = k-1 
    while pos >0 and li_i[pos-1]>li_i[pos]:
        li_i[pos-1],li_i[pos] = li_i[pos],li_i[pos-1]
        pos-=1
    return li_i

def InsertionSort_rec_num(li,k):
    
    if k>1:
        InsertionSort_rec(li,k-1)
        isort(li[:k],k)# Not using "li[:k] =" as li and li_i SHARE MEMORY (NUMPY)


def isort_num(li_i,k):
    
    # list li_i memory is different than the li as it's a slice of li BUT STILL they share memory
    # as swapping of values in the below loop reflects in li of InsertionSort_rec_num
    
    pos = k-1 
    while pos >0 and li_i[pos-1]>li_i[pos]:
        li_i[pos-1],li_i[pos] = li_i[pos],li_i[pos-1]
        pos-=1
    # return li_i   NOT REQUIRED AS IT AUTOMATICALLY GETS REFLECTED (NUMPY)

if __name__ == '__main__':
    
    # creating a reverse list
    
    li = [i for i in range(50,1,-1)]
    
    InsertionSort_rec(li,len(li))
    
    li_num = np.arange(50,0,-1)
    
    InsertionSort_rec_num(li_num,len(li_num))
    