# https://www.hackerrank.com/challenges/incorrect-regex
import re
n = int(input())
for i in range(n):
    ex=input()
    try:
        re.compile(ex)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
