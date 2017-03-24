# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

#!/bin/python3

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
# your code goes here
highest_score = score[0]
lowest_score = score[0]
highest_break_count = 0
lowest_break_count = 0
for i in range(1,n):
    if score[i] > highest_score:
        highest_break_count += 1
        highest_score = score[i]
    if score[i] < lowest_score:
        lowest_break_count += 1
        lowest_score = score[i]
print(highest_break_count, lowest_break_count)
        
