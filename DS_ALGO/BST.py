#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:21:05 2019

@author: siddharth
"""

class BST_node:
    def __init__(self,value=None):
        self.value = value
        
        if self.value == None:     
            self.left = None
            self.right = None            
        else:
            self.left = BST_node()
            self.right = BST_node()
    
    def isEmpty(self):
        if self.value:
            return False
        else:
            return True
        
    # Checks if the node is leaf or not
    def isleaf(self):
        if self.value!=None and self.left.isEmpty() and self.right.isEmpty():
            return True
        else:
            return False
        
    # Copies right child values to the current node
    def copyRight(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        
    # Inorder traversal
    def inorder(self):
        if self.value==None:
            return []     
        else:
            return self.left.inorder()+[self.value]+self.right.inorder()
    
    # Checks if val is present in the tree or not
    def find(self,val):
        if self.isEmpty():
            return False
        
        if self.value == val:
            return True
        
        elif self.value<val:
            return self.right.find(val)
        
        else:
            return self.left.find(val)
        
    # Insert value to the tree
    def insert(self,val):
        if self.isEmpty():
            self.value = val
            self.right = BST_node()
            self.left = BST_node()
        
        if self.value == val:
            return
        
        if val < self.value:
            self.left.insert(val)
            
        if val> self.value:
            self.right.insert(val)
            
    # Finds the max value
    def maxVal(self):
        
        if self.right.value!=None:
            return self.right.maxVal()
        else:
            return self.value
        
      
    # Delete value from the tree
    def delete(self,val):
        if val < self.value:
            self.left.delete(val)
        if val > self.value:
            self.right.delete(val)
        if self.value == val:
            if self.isleaf():
                self.value = None
                self.right = None
                self.left = None
            
            elif self.left.isEmpty():
                self.copyRight()
            else:
                self.value = self.left.maxVal()
                self.left.delete(self.left.maxVal())
        
        
    def __str__(self):
        return str(self.inorder())
    
    
    
if __name__ == '__main__':
    
    bst = BST_node()
    for i in [1,3,2,18,7,5,4,22,14]:
        bst.insert(i)
        
    print(bst)
    
    bst.insert(17)
    
    print(bst)
    
    bst.insert(4.5)
    
    print(bst)
    
    bst.delete(3)
    
    print(bst)
    
    bst.delete(14)
    
    print(bst)