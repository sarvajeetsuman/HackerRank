# https://www.hackerrank.com/challenges/repeated-string

#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
l = n//len(s)
r = n - l*len(s)
print(s.count('a')*l+s[:r].count('a'))
