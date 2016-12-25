# https://www.hackerrank.com/challenges/np-array-mathematics

import numpy
n,m = input().split()
n,m = int(n),int(m)
array_1 = []
array_2 = []
for i in range(n):
    array_1.append(list(map(int,input().split())))
for j in range(n): 
    array_2.append(list(map(int,input().split())))

array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)

print (array_1 + array_2)
print (array_1 - array_2)
print (array_1 * array_2)
print (array_1 // array_2)
print (array_1 % array_2)
print (array_1 ** array_2)
