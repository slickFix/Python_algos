#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:34:01 2019

@author: siddharth
"""

# Implementing Greatest Common Divisor

def gcd(m,n):
    if (m<n):
        (m,n) = (n,m)
    if (m%n==0):
        return n
    else:
        return gcd(n,m%n) # gcd(m,n) = gcd(n,m%n)
    

        
if __name__ == '__main__':
    m = int(input("enter 1st number: "))
    n = int(input("enter 2nd number: "))
    print("GCD of the numbers = "+ str(gcd(m,n)))
