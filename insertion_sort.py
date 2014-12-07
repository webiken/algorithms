#!/usr/bin/env python
A = [0, 1, 3, -2, 0, 1, 0, -3, 2, 3]

def insertion_sort(_array):
	for i in range(len(_array)):
		j = i
		while ((j > 0) and (_array[j] < _array[j-1])):
			_array[j], _array[j-1] = _array[j-1], _array[j]
			j = j - 1
	return _array

print insertion_sort(A)