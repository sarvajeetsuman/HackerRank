# https://www.hackerrank.com/challenges/string-construction

#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    print(len(set(s)))
