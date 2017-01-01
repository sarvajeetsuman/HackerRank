# https://www.hackerrank.com/challenges/camelcase

#!/bin/python3

import sys


s = input().strip()
charlst = list(s)
count = 0
for c in charlst:
    if c.isupper() :
        count+=1
print(count+1)

