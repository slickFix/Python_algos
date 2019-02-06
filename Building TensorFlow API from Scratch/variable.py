#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:35:29 2019

@author: siddharth
"""

import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')

path = os.getcwd()

import sys
sys.path.append(path)

from graph import *

class Variable():
    def __init__(self,initial_value=None):
        self.value = initial_value
        _default_graph.variables.append(self)