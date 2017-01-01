# https://www.hackerrank.com/challenges/mars-exploration

#!/bin/python3

import sys


S = input().strip()
n = len(S)//3
str = "SOS"*n
count = 0
for s,t in zip(S, str):
    if s != t:
        count += 1
print(count)


