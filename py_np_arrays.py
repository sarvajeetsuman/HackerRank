# https://www.hackerrank.com/challenges/np-arrays 

import numpy
a = list(map(float ,input().split()))
a = numpy.array(list(reversed(a)) , float)
print (a)
