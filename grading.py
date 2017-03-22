#!/bin/python3
# https://www.hackerrank.com/challenges/grading

import sys


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    # your code goes here
    if grade < 38 :
        print(grade)
    else:
        if ((grade//5 + 1) * 5) - grade < 3 :
            print((grade//5 + 1) * 5)
        else:
            print(grade)
