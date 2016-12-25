# https://www.hackerrank.com/challenges/np-concatenate

import numpy

n,m,p = input().split()
n = int(n)
m = int(m)
p = int(p)
array_1 = []
array_2 = []

for i in range(n):
    temp = list(map(int,input().split()))
    array_1.append(temp)
for i in range(m):
    temp = list(map(int, input().split()))
    array_2.append(temp)
    
array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)
print (numpy.concatenate((array_1, array_2)))
