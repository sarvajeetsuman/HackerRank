# https://www.hackerrank.com/challenges/py-the-captains-room

k = int(input())
lst = list(input().split())
lst = sorted(lst)
dict={}
for i in range(len(lst)):
    if lst[i] not in dict:
        dict[lst[i]]=1
    else:
        dict[lst[i]]=dict[lst[i]]+1
for item in dict:
    if dict[item] == 1:
        print(int(item))
