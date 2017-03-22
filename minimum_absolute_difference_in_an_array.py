#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here

a = sorted(a)
min_value = abs(a[0]-a[1])

for i in range(len(a)-1):
    if abs(a[i]-a[i+1]) < min_value:
        min_value = abs(a[i]-a[i+1])
print(min_value)

