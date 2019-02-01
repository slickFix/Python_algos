#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:05:57 2019
    
@author: siddharth
"""

import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()

import sys
sys.path.append(path)

from graph import *

class Operation:
    def __init__(self,input_nodes = None):
        self.input_nodes = input_nodes
        self.output = None
        
        # Append operation to the list of operations of the default graph
        _default_graph.operations.append(self)
        
    def forward(self):
        pass
    
    
    def backward(self):
        pass