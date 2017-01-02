# https://www.hackerrank.com/challenges/equality-in-a-array

n = int(input())
arr = [int(i) for i in input().strip().split()]
countdict = {}
for i in arr:
    if i in countdict:
        countdict[i] += 1
    else:
        countdict[i] = 1
maxe = 0 
lst = list(countdict.values())
print(n-max(lst))
