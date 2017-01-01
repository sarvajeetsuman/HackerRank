#https://www.hackerrank.com/challenges/mini-max-sum

#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

lst = [a,b,c,d,e]
minimum = min(lst)
maximum = max(lst)

total = sum(lst)

withoutminsum = total - minimum
withoutmaxsum = total - maximum

print(withoutmaxsum, withoutminsum)



