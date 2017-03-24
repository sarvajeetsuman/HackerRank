# https://www.hackerrank.com/challenges/angry-children
n = int(input())
k = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst = sorted(lst)
unfairness = lst[k-1]-lst[0]
i = 0
while i < (n-k+1) :
    if unfairness > (lst[i+k-1]-lst[i]):
        unfairness = (lst[i+k-1]-lst[i])
    i +=1
print(unfairness)
