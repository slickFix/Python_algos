#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:39:48 2019

@author: siddharth
"""

from heapq import heappush,heappop,heapify

class MinHeap:
    
    def __init__(self):
        self.heap = [] 
        
    def insertKey(self,val):
        heappush(self.heap,val)
        
    def parent(self,i):
        return abs((i-1)//2)
    
    # Decrease value of key at index 'i' to new_val 
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self,index,new_val):
        self.heap[index] = new_val
        
        while(index!=0 and self.heap[index]<self.heap[self.parent(index)]):
            self.heap[index],self.heap[self.parent(index)] = self.heap[self.parent(index)],self.heap[index]
            index = self.parent(index)
            
    def extractMin(self):
        return heappop(self.heap)
    
    
    def deleteIndex(self,index):
        self.decreaseKey(index,float("-inf"))
        self.extractMin()
        
    def getMin(self):
        return self.heap[0]
    
    def printHeap(self):
        for i in self.heap:
            print(i,end=' ')
        print()
    

if __name__=='__main__':
    
    heapObj = MinHeap()
    heapObj.insertKey(3) 
    heapObj.insertKey(2) 
    print("Heap before deleteIndex :")
    heapObj.printHeap()
    heapObj.deleteIndex(1) 
    heapObj.insertKey(15) 
    heapObj.insertKey(5) 
    heapObj.insertKey(4) 
    heapObj.insertKey(45)
    
    print("Heap :")
    heapObj.printHeap()
    print("Minimum heap object ",heapObj.getMin())
    