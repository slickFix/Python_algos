#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:06:34 2019

@author: siddharth
"""

import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()

import sys
sys.path.append(path)

class Graph():
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
        self.constants = [] 
        
    def as_default(self):
        global default_graph
        _default_graph = self