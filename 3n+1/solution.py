#!/usr/bin/env python

def solution(i, j):
    count = toRtn = 1
    for n in xrange(i, j+1):
        count = 1
        while n != 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = (3 * n) + 1
            count += 1
        toRtn = max(toRtn, count)
    return toRtn

print solution(100, 200)
print solution(201, 210)