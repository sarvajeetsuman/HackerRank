# https://www.hackerrank.com/challenges/jumping-on-the-clouds

#!/bin/python3

import sys
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

count = 0
i = 0
while i < n-3 :
    if c[i+1] == 0:
        if c[i+2] == 0:
            count +=1
            i += 2
        else:
            count+=1
            i += 1
    else:
        count += 1
        i +=2
print (count+1)
