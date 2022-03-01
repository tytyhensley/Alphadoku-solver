#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:25:34 2017

Name: Tyeece Hensley
Date: November 16,2017
"""
import math
import datetime


def get_board(csvfile): #function that reads board from csv file into a list of lists
    board=[]
    for line in csvfile:
        sublist =line.strip().split(',')
        board.append(sublist)
    return board

def in_row(board, row): #function that reads the letters present in a specific row in the board
    char_row=[]
    for x in range(len(board[row])):
        if(board[row][x]!='+'):
            char_row.append(board[row][x])
    return char_row

def in_column(board, column): #function that reads the letters present in a specific column in the board
    char_col=[]
    for x in range(len(board)):
        if(board[x][column]!='+'):
            char_col.append(board[x][column])
    return char_col


def in_sector(board, row, column): #function that reads the letters present in a specific sector in the board
    root=int(math.sqrt(len(board)))  
    k=root
    start_r=1
    while (start_r==1):
        if((row+1)<=k):
            start_r=k-root
            end_r=k
            break
        else:
            k=k+root
    y=root
    start_c=1
    while (start_c==1):
        if((column+1)<=y):
            start_c=y-root
            end_c=y
            break
        else:
            y=y+root
    char_sect=[]
    for r in range(start_r,end_r):
        for c in range(start_c,end_c):
            if(board[r][c]!='+'):
                char_sect.append(board[r][c])
    return char_sect

def get_blank(board): #function that gets the coordinates for one blank character present in the board and returns false if there is none 
    char_blnk=[]
    for x in range(len(board)):
        for y in range (len(board)):
            if (board[x][y]=='+'):
                break
        if (board[x][y]=='+'):
            break
    if (board[x][y]=='+'):
        char_blnk.append(x)
        char_blnk.append(y)
        return char_blnk
    else:
        return char_blnk
     
def print_board(board):#function that prints the board
        for x in range(len(board)):
            print(('+-'* len(board))+'+')
            for y in range (len(board)):
                if (board[x][y]=='+'):
                    print('| ',end="")
                else:
                    print('|'+board[x][y],end="")            
            print('|')
        print(('+-'* len(board))+'+') 
        
def valid_characters(board):#function that gives a list of characters that can be used in the board depending on its size
    char_val=[]
    for x in range(len(board)):
        c=chr(97+x)
        char_val.append(c)
    return char_val

def solve(board):#function that solves the alphadoku puzzle
    char_blnk=get_blank(board)
    if (bool(char_blnk)==False):
        return True
    else:
        char_row=in_row(board,char_blnk[0])
        char_col=in_column(board,char_blnk[1])
        char_sect=in_sector(board,char_blnk[0],char_blnk[1])
        char_val=valid_characters(board)
        for a in char_val:
            if((a  not in char_row )and (a not in char_col) and (a not in char_sect))==True:#test if a letter is present within the row,columnand sector before placing it
                x=char_blnk[0]
                y=char_blnk[1]
                previous=board[x][y]
                board[x][y]=a
                if (solve(board)==True):#recurse
                    return True
                else: 
                    board[x][y]=previous
        return False

fp=open('25x25-1.csv',mode='r')
board=get_board(fp)
fp.close()
print("Initial board:")
print_board(board)
x=datetime.datetime.now()
solve(board)
y=datetime.datetime.now()
print("\nSolved board:")
print_board(board)
print("\nTime taken to solve:",y-x)#prints how long the puzzle took to solve