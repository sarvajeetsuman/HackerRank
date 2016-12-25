import numpy
n = int(input())
array_1 = []
for _ in range(n):
    temp = list(map(float,input().split()))
    array_1.append(temp)
print(numpy.linalg.det(array_1))
