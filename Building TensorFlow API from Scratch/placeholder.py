#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 21:55:09 2019

@author: siddharth
"""

import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()

import sys
sys.path.append(path)

from graph import *

class Placeholder():
    def __init__(self):
        self.value = None
        _default_graph.placeholders.append(self)