# https://www.hackerrank.com/challenges/greedy-florist

N,K = input().split()
N,K = int(N), int(K)
lst = list(map(int, input().split()))
lst = sorted(lst)
required = 0
if N <= K:
    print(sum(lst))
else:
    length = len(lst)
    for i in range(length):
        required = required + (i//K + 1)*lst[length-i-1]
    print(required)
