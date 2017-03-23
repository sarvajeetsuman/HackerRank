# https://www.hackerrank.com/challenges/icecream-parlor
test = int(input())
for t in range(test):
    m = int(input())
    n = int(input())
    flavour = list(map(int, input().split()))
    for i in range(len(flavour) - 1):
        j = i + 1
        while j<len(flavour):
            if flavour[i] + flavour[j] == m:
                print("%d %d"% (i+1, j+1))
                break
            j += 1
    
