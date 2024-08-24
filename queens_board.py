from os import *
from sys import *
from collections import *
from math import *


def nQueens(n):
    results = []
    path = [[0 for _ in range(n)]for _ in range(n)]
    q = 0

    #check valid
    def is_valid(x, y):

        if path[x][y] == 1:
            return False
        #check row and col
        for i in range(n):
            if (path[x][i] == 1) or (path[i][y] == 1):
                return False
        #check diaganols
        for i in range(n):
            if x + i < n and y + i < n and path[x + i][y + i] == 1:
                return False
            if x - i >= 0 and y - i >= 0 and path[x - i][y - i] == 1:
                return False
            if x + i < n and y - i >= 0 and path[x + i][y - i] == 1:
                return False
            if x - i >= 0 and y + i < n and path[x - i][y + i] == 1:
                return False
        return True

    def backtrack(row, q, path):
        if q == 2:
            result = []
            for r in path:
                result.extend(r)
            results.append(result)
            return
        if row >= n:
            return
        for col in range(n):
            if is_valid(row, col):
                path[row][col] = 1
                backtrack(row + 1, q + 1, path)
                path[row][col] = 0
        backtrack(row + 1, q, path)
    
    backtrack(0, q, path)
    return results