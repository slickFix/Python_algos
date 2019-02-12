#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:10:17 2019

@author: siddharth
"""

import TF_API as tf


tf.Graph().as_default()

a = tf.Constant(15)
b = tf.Constant(5)


prod = tf.Multiply(a,b)

sum_no = tf.Add(a,b)

res = tf.Divide(prod,sum_no)

session = tf.Session()

out = session.run(res)

print(out)