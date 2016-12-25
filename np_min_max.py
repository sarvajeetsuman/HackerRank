# https://www.hackerrank.com/challenges/np-min-and-max

import numpy
n,m = input().split()
n,m = int(n),int(m)
array_1 = []
for i in range(n):
    temp = list(map(int, input().split()))
    array_1.append(temp)
mina = numpy.min(array_1, axis = 1)
print(numpy.max(mina))
