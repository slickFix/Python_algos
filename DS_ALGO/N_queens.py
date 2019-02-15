#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:37:05 2019

@author: siddharth
"""


def initializeBoard(board,n):
    for i in ['queen','row','col','nwtose','swtone']:
        board[i]={}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0

def printBoard(board):
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]))

if __name__ == '__main__':
    
    n = input('Enter the number of queens :')
    board = {}
    initializeBoard(board,n)