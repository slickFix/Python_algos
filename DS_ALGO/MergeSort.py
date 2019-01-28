#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:07:20 2019

@author: siddharth
"""

import numpy as np

def MergeSort(li):
    
    
    if len(li)==1:
        return li
    
    li_l = MergeSort(li[:len(li)//2])
    li_r = MergeSort(li[len(li)//2:])
    
    return Merge(li_l,li_r)

def Merge(li_l,li_r):
    
    ret_li = []
    
    i,j = 0,0
    
    while i<len(li_l) or j<len(li_r):
        if i == len(li_l):
            ret_li.append(li_r[j])
            j+=1
            continue
        
        if j == len(li_r):
            ret_li.append(li_l[i])
            i+=1
            continue
        
        if li_l[i] < li_r[j]:
            ret_li.append(li_l[i])
            i+=1
            continue
        else :
            ret_li.append(li_r[j])
            j+=1
            
    return ret_li
            
        

if __name__ == '__main__':
    
    
    li = [i for i in range(100,2,-2)]
    
    sortedList = MergeSort(li)