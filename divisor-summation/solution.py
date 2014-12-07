#!/usr/bin/env python

def solution(N):
    to_return = 0
    for i in xrange(1, N):
        if N % i == 0:
            to_return += i
    return to_return

print solution(2)
print solution(10)
print solution(20)