# https://www.hackerrank.com/challenges/insertionsort2

num = int(input())
array = list(map(int, input().split()))
temp = 0
for i in range(1, len(array)):
    k = i
    for j in range(i):
        if array[k] < array[i-j-1]:
            temp = array[k]
            array[k] = array[i-j-1]
            array[i-j-1] = temp
            k = i-j-1
    for t in array:
        print(t, end=' ')
    print()
