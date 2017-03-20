#!/bin/python3

import sys

def min_string(n):
    if(n==2):
        return 'min(int, int)'
    else:
        return 'min(int, %s)' % min_string(n-1)

n = int(input().strip())
str = min_string(n)
print (str)
