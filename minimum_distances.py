# https://www.hackerrank.com/challenges/minimum-distances

#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
element = {}
minlist = []
for e in A:
    if e in element:
        minlist.append(A[element[e]+1:].index(e)+element[e]+1- element[e])
    else:
        element[e] = A.index(e)
if len(minlist) == 0 :
    print(-1)
else:
    print(min(minlist))

