# https://www.hackerrank.com/challenges/between-two-sets

#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

maximum_of_a = max(a)
minimum_of_b = min(b)
flag1 = 0
flag2 = 0
having_factor_a = []
for i in range(maximum_of_a, minimum_of_b+1):
    for j in a:
        if i%j ==0:
            flag1 = 0
            continue
        else:
            flag1 = 1
            break
    if flag1 == 0:
        having_factor_a.append(i)
#print(having_factor_a)
having_factor_b = []
for i in having_factor_a:
    for j in b:
        if j%i == 0:
            flag2 = 0
            continue
        else:
            flag2 = 1
            break
    if flag2 == 0:
        having_factor_b.append(i)
print(len(having_factor_b))


