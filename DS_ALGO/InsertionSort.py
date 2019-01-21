#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:17:02 2019

@author: siddharth
"""

import numpy as np

def InsertionSort(np_li):
    
    li = np_li
    
    for i in range(1,len(li)):
        
        pos = i
        
        while pos>0 and li[pos-1]>li[pos]:
            li[pos-1],li[pos] = li[pos],li[pos-1]
            pos-=1
    
    return li


if __name__ == "__main__":
    
    # gettting the random array list from -100 to 100 with 50 elements
    
    np_li = np.random.randint(-100,100,50)
    li = np_li.tolist()
    
    
    sort_li = InsertionSort(np_li)
    
