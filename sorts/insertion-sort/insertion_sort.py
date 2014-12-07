#!/usr/bin/env python

def insertion_sort(_array):
	global count
	for i in range(len(_array)):
		count = count + 1
		j = i
		print 'j={} j-1={}..{} {}'.format(j, j-1, _array[j], _array[j-1])
		while ((j > 0) and (_array[j] < _array[j-1])):
			count = count + 1
			print 'j={} j-1={}>>{} {}'.format(j, j-1, _array[j], _array[j-1])
			_array[j], _array[j-1] = _array[j-1], _array[j]
			j = j - 1
	return _array


A = [3, 2, 1]
count = 0
print insertion_sort(A)
print '{}'.format(count)

A = [4, 3, 2, 1]
count = 0
print insertion_sort(A)
print '{}'.format(count)

A = [5, 4, 3, 2, 1]
count = 0
print insertion_sort(A)
print '{}'.format(count)