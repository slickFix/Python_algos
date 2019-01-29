#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:38:13 2019

@author: siddharth
"""

import numpy as np


def QuickSort(li):
    
    if len(li)<=1:
        return li
    
    i = 0
    pivot = li[0]
    for j in range(1,len(li)):
        if li[j]<pivot:
            i+=1
            li[i],li[j] = li[j],li[i]
    
    li[i],li[0] = li[0],li[i]
    if i!=0:
         li[0:i] = QuickSort(li[0:i])
     
    li[i+1:] = QuickSort(li[i+1:])
    return li


if __name__ == '__main__':
    
    
    li = [i for i in range(25,20,-3)]
    li = li + [2,2,3,1]*2
    li = li+ [i for i in range(50,40,-3)]
    
    sorted_li = QuickSort(li)
    