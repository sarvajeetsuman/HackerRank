# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i=0
energy = 100
while True :
    i = (i+k)%n
    if c[i] == 0:
        energy = energy - 1
    else:
        energy = energy - 3   
    if i == 0 :
        break
print(energy)
