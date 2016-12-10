#https://www.hackerrank.com/challenges/py-set-discard-remove-pop
n = int(input())
s = set(map(int, input().split())) 
num = int(input())
for i in range(num):
    lst = input().split()
    if(len(lst)==1 and lst[0]=='pop'):
        s.pop()
    if(len(lst)==2 and lst[0]=='remove'):
        s.remove(int(lst[1]))
    if(len(lst)==2 and lst[0]=='discard'):
        s.discard(int(lst[1]))
print(sum(s))       
