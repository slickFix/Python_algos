#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:02:54 2019

@author: siddharth
"""

def reverse_str(string):
    
    # creating stack    
    stack = []    
    
    for i in range(len(string)):
        stack.append(string[i])
    
    return_str = ""
    
    for i in range(len(stack)):
        return_str += stack.pop()
    
    return return_str

if __name__ == "__main__":
    string = input("Enter the string you want to reverse : ")
    
    option = int((input("\nEnter 1 to reverse using stack and 2 to reverse using list iterator : ")))
    
    if option ==1:
        rev_string = reverse_str(string)
    
    else :
        rev_string = string[::-1]
        
    print("\n",rev_string,sep='\n')