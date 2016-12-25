import numpy

lst = list(map(float, input().split()))
num = int(input())

print(numpy.polyval(lst,num))
