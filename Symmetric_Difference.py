# https://www.hackerrank.com/challenges/symmetric-difference
n1=int(input())
arr1=set(list(map(int,input().split())))
n2=int(input())
arr2=set(list(map(int,input().split())))
final=[]
final=(arr1.union(arr2)).difference(arr1.intersection(arr2))
final=sorted(final)
for i in range(len(final)):
    print(final[i])
