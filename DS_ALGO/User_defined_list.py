#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:08:59 2019

@author: siddharth
"""

class Li_node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
    def isempty(self):
        return (self.value==None)
    
    def append(self,val):
        if self.isempty():
            self.value = val
        
        elif self.next==None:
            newnode = Li_node(val)
            self.next = newnode
        
        else:
            self.next.append(val)
        
        
    
    
    
    
if __name__ == '__main__':
    