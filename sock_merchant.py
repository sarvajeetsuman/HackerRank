# https://www.hackerrank.com/challenges/sock-merchant

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
sockscount = {}
for sock in c:
    if sock in sockscount:
        sockscount[sock] += 1
    else:
        sockscount[sock] = 1
pairs_sold = 0
for e in sockscount:
    pairs_sold += sockscount[e] // 2
print(pairs_sold)
