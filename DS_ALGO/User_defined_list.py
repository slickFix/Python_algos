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
            
    def insert_first(self,val):
        
        if self.isempty():
            self.value = val
            return
        
        newnode = Li_node(val)    
        self.value,newnode.value = newnode.value,self.value
        self.next,newnode.next  =newnode,self.next
        
    def delete(self,val):
        if self.isempty():
            return
        
        if self.value == val:
            self.value = None
            
            if self.next == None:
                return
            else:
                self.value,self.next.value = self.next.value,self.value
                self.next.next,self.next = None,self.next.next 
                # order matters!!! if self.next is updated 1st then self.next.next points to diff
                # location than thought of
        else:
            if self.next!=None:
                self.next.delete(val)
                if self.next.value == None: # for the case when val is the last element of list
                    self.next = None
    
    def __str__(self):
        li = []
        if self.value == None:
            return str(li)
        
        temp = self
        li.append(temp.value)
        
        while(temp.next !=None):
            temp = temp.next
            li.append(temp.value)
        return str(li)
       
    
if __name__ == '__main__':
    li = Li_node(0)
    for i in range(1,11):
        li.append(i)
        
    print(li)
    
    li.delete(3)
    
    print(li)
    
    li.insert_first(-1)
    
    print(li)