#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:12:42 2019

@author: siddharth
"""


import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')

path  = os.getcwd()

import sys
sys.path.append(path)


from graph import *
from placehoder import *
from constant import *
from variable import *
from operation import *

def topology_sort(operation):
    ordering = [] 
    visited_nodes = set()
    
    def recursive_helper(node):
        if isinstance(node,Operation):
            for input_node in node.input_nodes:
                if input_node not in visited_nodes:
                    recursive_helper(input_node)
                    
        visited_nodes.add(node)
        ordering.append(node)
        
    # recursive dfs
    recursive_helper(operation)
    
    return ordering

class Session():
    
    def run(self,operation,feed_dict={}):
        nodes_sorted = topology_sort(operation)
        
        for node in nodes_sorted:
            if type(node) == Placeholder:
                node.output = feed_dict[node]
            elif type(node) == Variable  or type(node) ==  Constant:
                node.output = node.value
            else:
                inputs = [node.output for node in node.input_nodes]
                node.output = node.forward(*inputs)
                
        return operation.output