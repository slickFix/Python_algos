#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:06:34 2019

@author: siddharth
"""

class Graph():
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
        self.constants = [] 
        
    def as_default(self):
        global default_graph
        _default_graph = self