# https://www.hackerrank.com/challenges/np-transpose-and-flatten 

import numpy
n,m = input().split()
n=int(n)
marr = []
for i in range(n):
    arr = list(map(int,input().split()))
    marr.append(arr)
marr = numpy.array(marr)
print(numpy.transpose(marr))
print(marr.flatten())
