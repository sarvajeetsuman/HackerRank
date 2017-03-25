# https://www.hackerrank.com/challenges/permutation-equation

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    ind = arr.index(i+1)
    print(arr.index(ind+1)+1)
    

