# https://www.hackerrank.com/challenges/extra-long-factorials

#!/bin/python3

import sys


n = int(input().strip())
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(factorial)
