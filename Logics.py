#!/usr/bin/env python
# coding: utf-8

# # 2048 Game Logics

import random

def start_game(n=4):
    mat = [[0 for i in range(n)] for i in range(n)]
    return mat

def add_new_2(mat):
    n = len(mat)
    r = random.randint(0,n-1)
    c = random.randint(0,n-1)
    while mat[r][c] != 0:
        r = random.randint(0,n-1)
        c = random.randint(0,n-1)
    mat[r][c] = 2

def get_curr_state(mat):
    n = len(mat)
    # Anywhere 2048 is present
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2048:
                return 1
            
    # Anywhere 0 is present
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                return 0
    # Checking every row & column except last ones
    for i in range(n-1):
        for j in range(n-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 0
    # Checking last row
    for j in range(n-1):
        if mat[n-1][j] == mat[n-1][j+1]:
                return 0
    # Checking last column
    for i in range(n-1):
        if mat[i][n-1] == mat[i+1][n-1]:
                return 0
            
    return -1

# MOVEMENT Functions

def upHelper(grid,  i, j):
    n = len(grid)
    if i==0:
        return
    if grid[i-1][j] == 0:
        grid[i-1][j], grid[i][j] = grid[i][j], grid[i-1][j]
        upHelper(grid, i-1, j)
    if grid[i-1][j] == grid[i][j]:
        grid[i-1][j] = 2*grid[i][j]
        grid[i][j] = 0
        upHelper(grid, i-1, j)

def move_up(grid):
    n = len(grid)
    change = False
    for i in range(1, n):
        for j in range(n):
            if grid[i][j]:
                change = True
                upHelper(grid, i, j)
    return change

def downHelper(grid,  i, j):
    n = len(grid)
    if i==n-1:
        return
    if grid[i+1][j] == 0:
        grid[i+1][j], grid[i][j] = grid[i][j], grid[i+1][j]
        downHelper(grid, i+1, j)
    if grid[i+1][j] == grid[i][j]:
        grid[i+1][j] = 2*grid[i][j]
        grid[i][j] = 0
        downHelper(grid, i+1, j)

def move_down(grid):
    n = len(grid)
    change = False
    for i in range(n-2, -1, -1):
        for j in range(n):
            if grid[i][j]:
                change = True
                downHelper(grid, i, j)
    return change

def rightHelper(grid,  i, j):
    n = len(grid)
    if j==n-1:
        return
    if grid[i][j+1] == 0:
        grid[i][j+1], grid[i][j] = grid[i][j], grid[i][j+1]
        rightHelper(grid, i, j+1)
    if grid[i][j+1] == grid[i][j]:
        grid[i][j+1] = 2*grid[i][j]
        grid[i][j] = 0
        rightHelper(grid, i, j+1)

def move_right(grid):
    n = len(grid)
    change = False
    for j in range(n-2, -1, -1):
        for i in range(n):
            if grid[i][j]:
                change = True
                rightHelper(grid, i, j)
    return change

def leftHelper(grid,  i, j):
    n = len(grid)
    if j==0:
        return
    if grid[i][j-1] == 0:
        grid[i][j-1], grid[i][j] = grid[i][j], grid[i][j-1]
        leftHelper(grid, i, j-1)
    if grid[i][j-1] == grid[i][j]:
        grid[i][j-1] = 2*grid[i][j]
        grid[i][j] = 0
        leftHelper(grid, i, j-1)

def move_left(grid):
    n = len(grid)
    change = False
    for j in range(1,n):
        for i in range(n):
            if grid[i][j]:
                change = True
                leftHelper(grid, i, j)
    return change

