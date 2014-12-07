#!/usr/bin/env python

"""
This solution is based off the solution written in Java
found @ http://stackoverflow.com/a/12329821/1158977
"""

A = [0, 1, 3, -2, 0, 1, 0, -3, 2, 3]

def solution(_array):
    depth = 0
    P = Q = R = -1
    P = 0
    for i in range(len(_array)):
        if Q < 0 and A[i] >= A[i-1]:
            Q = i -1
        if ((Q >= 0 and R < 0)) and (A[i] <= A[i-1] or i+1 == len(_array)):
            R = i - 1
            depth = max(depth, min(A[P]-A[Q], A[R]-A[Q]))
            P = i -1
            Q = R = -1

    if depth == 0: return -1
    return depth

if __name__ == '__main__':
    print solution(A)