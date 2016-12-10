#https://www.hackerrank.com/challenges/py-set-union
n1 = int(input())
e=set(list(map(int,input().split())))
n2= int(input())
f = set(list(map(int,input().split())))
print(len(e.union(f)))
