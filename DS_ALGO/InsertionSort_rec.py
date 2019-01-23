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
        li[:k] = isort(li[:k],k)  


def isort(li_i,k):
    
    pos = k-1 
    while pos >0 and li_i[pos-1]>li_i[pos]:
        li_i[pos-1],li_i[pos] = li_i[pos],li_i[pos-1]
        pos-=1
    return li_i

if __name__ == '__main__':
    
    # creating a reverse list
    
    li = [i for i in range(50,1,-1)]
    
    InsertionSort_rec(li,len(li))