# https://www.hackerrank.com/challenges/hackerrank-in-a-string

#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    hr_str = 'hackerrank'
    hr_length = len(hr_str)
    ind = -1
    flag = True
    for i in range(hr_length):
        try:
            ind = s.index(hr_str[i])
        except:
            ind = -1
        if ind <=-1:
            flag = False
            break
        else:
            s =s[ind+1 :] 
    if flag == True:
        print("YES")
    else:
        print("NO")
            


