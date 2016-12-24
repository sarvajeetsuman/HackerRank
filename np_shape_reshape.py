# https://www.hackerrank.com/challenges/np-shape-reshape

import numpy
a = numpy.array(list(map(int,input().split())))
print (numpy.reshape(a,(3,3)))
