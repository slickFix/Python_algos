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
    
    def inorder(self):
        if self.value==None:
            return []
        
        else:
            return self.left.inorder()+[self.value]+self.right.inorder()
        
    def __str__(self):
        return str(self.inorder())