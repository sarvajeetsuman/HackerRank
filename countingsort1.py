# https://www.hackerrank.com/challenges/countingsort1

n = int(input())
lst = list(map(int, input().split()))
maxi = max(lst) + 1
new_list = [0]*maxi
for element in lst:
    new_list[element] = new_list[element] + 1
for element in new_list:
    print(element, end=' ')
    

