#!/bin/python3
# https://www.hackerrank.com/challenges/marcs-cakewalk
 
import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
# your code goes here
calories = sorted(calories)
dist = 0

for i in range(n):
    dist = dist + (calories[n-i-1] * (2**i))
print(dist)

