# https://www.hackerrank.com/challenges/np-sum-and-prod

import numpy
n,m = input().split()
n,m = int(n),int(m)
array_1 = []
for i in range(n):
    temp = list(map(int, input().split()))
    array_1.append(temp)
array_1 = numpy.array(array_1)
array_2 = numpy.sum(array_1, axis = 0)
print (numpy.prod(array_2))
