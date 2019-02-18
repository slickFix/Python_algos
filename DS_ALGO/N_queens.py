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

def free(i,j,board):
    return (board['queen'][i]==-1 and board['row'][i]==0 and board['col'][i]==0 \
            and board['nwtose'][i-j]==0 and board['swtone'][i+j]==0)

def addQueen(i,j,board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][i-j] = 1
    board['swtone'][i+j] = 1
    
def removeQueen(i,j,board):
    board['queen'][i]=-1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][i-j] = 0
    board['swtone'][i+j] = 0
    

    
if __name__ == '__main__':
    
    n = input('Enter the number of queens :')
    board = {}
    initializeBoard(board,n)
    if placeQueens(0,board):
        printBoard(board)
    