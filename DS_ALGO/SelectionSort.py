#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:49:25 2019

@author: siddharth
"""
import numpy as np

def SelectionSort(li):
    
    for i in range(0,len(li)-1):
        smallest_in = i
        for j in range(i+1,len(li)):
            if li[j]<li[smallest_in]:
                smallest_in = j
        if smallest_in != i:
            li[i],li[smallest_in] = li[smallest_in],li[i]
    
    return li
    

if __name__ == '__main__':
    
    
    #creating random list of 25 numbers where each number is from -100 to 100
    li = np.random.randint(-100,100,25)
    
    li = li.tolist()
    
    print('original list',li)
    print()
    s_sort_list = SelectionSort(li)
    
    print('sorted list',s_sort_list)
    
    li == s_sort_list