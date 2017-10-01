#!/usr/bin/python
i = 4
d = 4.0
s = 'HackerRank '

import sys
lines = sys.stdin.readlines()
# Declare second integer, double, and String variables.
ii,dd,ss = int, float, str
# Read and save an integer, double, and String to your variables.
ii = int(lines[0].strip())
dd = float(lines[1].strip())
ss = str(lines[2].strip())    
# Print the sum of both integer variables on a new line.
print(i+ii)
# Print the sum of the double variables on a new line.
print(d+dd)
# Concatenate and print the String variables on a new line
print(s+ss)
# The 's' variable above should be printed first.