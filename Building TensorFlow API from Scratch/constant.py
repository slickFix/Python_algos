#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:01:51 2019

@author: siddharth
"""

import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')

path = os.getcwd()

import sys
sys.path.append(path)

from graph import *

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