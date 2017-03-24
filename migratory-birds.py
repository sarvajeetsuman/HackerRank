# https://www.hackerrank.com/challenges/migratory-birds

#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
array = [0]*6
for element in types:
    array[element] += 1
frequent_type = 0
maxm = 0
for i in range(1,6):
    if array[i] > maxm:
        frequent_type = i
        maxm = array[i]
print(frequent_type)
