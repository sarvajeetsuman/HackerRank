# https://www.hackerrank.com/challenges/countingsort2

n = int(input())
lst = list(map(int, input().split()))
maxi = max(lst) + 1
new_list = [0]*maxi
for element in lst:
    new_list[element] = new_list[element] + 1
for i in range(len(new_list)):
    for j in range(new_list[i]):
        print(i, end=' ')
