#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:56:26 2019

@author: siddharth
"""

import numpy as np

def BinarySearch_rec(li,l,r,val):
    
    if(l>r):
        return False
    
    mid = (l+r )//2
    
    if li[mid]==val:
        return mid
    
    elif li[mid]>val:
        return BinarySearch_rec(li,l,mid-1,val)
    
    elif li[mid]<val:
        return BinarySearch_rec(li,mid+1,r,val)
    
    
    
    
if __name__ == '__main__':
    
    #creating array from -100 to 100
    
    li = np.random.randint(-100,100,90)
    li = np.sort(li)
    li = li.tolist()
    
    val = int(input("Enter the number between -100 to 100 to find : "))
    
    print(BinarySearch_rec(li,0,len(li)-1,val))