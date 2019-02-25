#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:27:41 2019

@author: siddharth
"""

def neighbours(s,b_size):
    
    ax = s[0]
    ay = s[1]
    
    ret_li = [] 
    
    if ax-2 >= 0 and ay+1<b_size:
        ret_li.append((ax-2,ay+1))
    
    if ax-2 >= 0 and ay-1>=0:
        ret_li.append((ax-2,ay-1))
        
    if ax+2 < b_size and ay+1<b_size:
        ret_li.append((ax+2,ay+1))
    
    if ax+2 < b_size and ay-1>=0:
        ret_li.append((ax+2,ay-1))
    
    if ay-2 >= 0 and ax+1<b_size:
        ret_li.append((ax+1,ay-2))
    
    if ay-2 >= 0 and ax-1>=0:
        ret_li.append((ax-1,ay-2))
    
    if ay+2 < b_size and ax+1<b_size:
        ret_li.append((ax+1,ay+2))
    
    if ay+2 < b_size and ax-1>=0:
        ret_li.append((ax-1,ay+2))
    
    return ret_li

def explore(s,t,b_size):
    sx = s[0]
    sy = s[1]
    tx = t[0]
    ty = t[1]
    
    marked_board = [[0 for i in range(b_size)] for i in range(b_size)]
    marked_board[sx][sy]=1
    q = [s]
    
    while q !=[]:
        ax,ay = q.pop()
        for (nx,ny) in neighbours((ax,ay),b_size):
            if !marked_board[nx][ny]:
                marked_board[nx][ny] = 1
                q.insert(0,(nx,ny))
            
        


if __name__ == '__main__':
    b_size = int(input('Enter the board dim(square): '))
    
    sx,sy = input('Enter the Knight start position: ').split()
    tx,ty = input('Enter the Knight target position: ').split()
    
    print('The target postion is possible or not ',explore((sx,sy),(tx,ty),b_size))
    