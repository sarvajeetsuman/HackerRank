# https://www.hackerrank.com/challenges/polar-coordinates

import cmath
n = complex(input())
lst=cmath.polar(n)
for i in lst:
    print(i)

