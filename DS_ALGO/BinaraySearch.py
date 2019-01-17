#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:11:12 2019

@author: siddharth
"""

import numpy as np

def BinarySearch(li,val):
    
    i = 0
    j = len(li)-1
    
    step = 1
    while(i<=j):
        mid = (i+j)// 2
        
        print(f"step no {step}")
        step+=1
        
        if li[mid]==val:
            return True
        elif li[mid]>val:
            j=mid-1
        elif li[mid]<val:
            i=mid+1
        else :
            return False
    return False
            
    
    

if __name__=='__main__':
    
    #creating 1 to  100 array
    li = np.random.randint(-100,100,90)
    li = np.sort(li)
    li = li.tolist()
    
    val = int(input("Enter the value between -100 and 100 to search  : "))
    
    print(BinarySearch(li,val))
    