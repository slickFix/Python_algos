#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:13:52 2019

@author: siddharth
"""



import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()


import sys
sys.path.append(path)

from operation import *

from graph import *

class BinaryOperation(Operation):
    def __init__(self,a,b):
        super().__init__([a,b])
        

