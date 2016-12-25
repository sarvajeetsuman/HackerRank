import numpy
n,m = input().split()
n,m = int(n),int(m)
array_1 = []
for _ in range(n):
    temp = list(map(int,input().split()))
    array_1.append(temp)

print (numpy.mean(array_1, axis = 1))
print (numpy.var(array_1, axis = 0))
print (numpy.std(array_1, axis = None))
