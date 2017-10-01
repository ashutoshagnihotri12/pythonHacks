#!/bin/python
import sys
n = int(raw_input().strip())    # take the number of elements in the array as input
arr = map(int,raw_input().strip().split(' '))    # the array
arr = ' '.join(map(str,arr[::-1]))    # flattening the reversed array
print(arr)
