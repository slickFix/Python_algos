#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:10:17 2019

@author: siddharth
"""



import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()


import sys
sys.path.append(path)


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
    
class BinaryOperation(Operation):
    def __init__(self,a,b):
        super().__init__([a,b])
        

class Add(BinaryOperation):
    """ add element wise , a+b """
    
    def forward(self,a,b):
        return a+b
    
    def backward(self,a,b):
        pass
    

class Multiply(BinaryOperation):
    """ multiply element wise, a*b """
    
    def forward(self,a,b):
        return a*b
    
    def backward(self,a,b):
        pass
    
    
class Divide(BinaryOperation):
    """ divide element wise, a/b """
    
    def forward(self,a,b):
        import numpy as np
        return np.true_divide(a,b)
    
    def backward(self,a,b):
        pass
    
class MatMul(BinaryOperation):
    """ muiltiply two matrices a and b , a*b """
    
    def forward(self,a,b):
        
        import numpy as np
        
        return np.dot(a,b)
    
    def backward(self,a,b):
        pass

class Constant():
	def __init__(self,value=None):
	    self.__value = value
	    _default_graph.constants.append(self)
	    
	    
	@property
	def value(self):
	    return self.__value

	@value.setter
	def value(self,value):
	    raise ValueError("Can't reassign value.")      

class Graph():
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
        self.constants = [] 
        
    def as_default(self):
        global _default_graph
        _default_graph = self


class Placeholder():
    def __init__(self):
        self.value = None
        _default_graph.placeholders.append(self)



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

class Variable():
    def __init__(self,initial_value=None):
        self.value = initial_value
        _default_graph.variables.append(self)