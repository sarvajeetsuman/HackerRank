# https://www.hackerrank.com/challenges/the-hurdle-race
#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
maxi = max(height)
if maxi <= k :
    print(0)
else:
    print(maxi -k)
