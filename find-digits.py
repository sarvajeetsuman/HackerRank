#https://www.hackerrank.com/challenges/find-digits
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lst = list(str(n))
    count = 0
    for i in range(len(lst)):
        if int(lst[i])!=0 and n%int(lst[i]) == 0:
            count += 1
    print(count)
