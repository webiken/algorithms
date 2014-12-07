#! /usr/bin/env python

A = [None]*10
A[0] = 0
A[1] = 1
A[2] = 3
A[3] = -2
A[4] = 0
A[5]  = 1
A[6] = 0
A[7] = -3
A[8] = 2
A[9] = 3



def solution(_array):
    _data = dict()
    _p,_q,_r = -1,-1,-1
    for i in xrange(len(_array)):
        p = _array[i]
        try:
            p1 = _array[i+1]
        except IndexError as e:
            break
        if p < p1:
            _p = i
            for j in xrange(i+2, len(_array)):
                p2 = _array[j]
                if p1 < p2:
                    p1 = p2
                    continue
                elif p1 > p2 and _q == -1:
                    p1 = p2
                    _q = j
                else:
                    _r = j
                    _data[','.join(str(n) for n in (_p,_q,_r))] = min(A[_p] - A[_q], A[_r] - A[_q])

    if len(_data) > 1:
        import operator
        return sorted(_data.items(), key=operator.itemgetter(0))[0]
    return -1

if __name__ == '__main__':
    print solution(A)