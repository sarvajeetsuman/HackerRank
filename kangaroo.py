#!/bin/python3
# https://www.hackerrank.com/challenges/kangaroo

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if abs(v2 - v1) == 0 :
    print("NO")
else:
    t = (x1 - x2) / (v2 -v1)
    if int(t) > 0:
        if t%int(t) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
