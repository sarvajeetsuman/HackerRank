# https://www.hackerrank.com/challenges/py-set-mutations
n = int(input())
A = set(list(map(int,input().split())))
num = int(input())
for i in range(num):
    op = list(input().split())
    N = set(list(map(int,input().split())))
    if(op[0]=='intersection_update'):
        A.intersection_update(N)
    if(op[0]=='update'):
        A.update(N)
    if(op[0]=='symmetric_difference_update'):
        A.symmetric_difference_update(N)
    if(op[0]=='difference_update'):
        A.difference_update(N)
print(sum(A))
