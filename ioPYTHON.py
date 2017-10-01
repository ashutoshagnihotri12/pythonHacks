#!/usr/bin/python
import sys
inFile = sys.argv[1]
f = open(inFile,'r')
# for l in f:
    # print(l.strip())
# Now with standard input
# lines = sys.stdin.readlines()
lines = f.readlines()
# for l in sys.stdin:
# 	print(l.strip())
print(lines)
print(float(lines[1].strip()))
