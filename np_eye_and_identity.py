# https://www.hackerrank.com/challenges/np-eye-and-identity

import numpy
n,m = input().split()
n,m = int(n), int(m)
print(numpy.eye(n,m))

