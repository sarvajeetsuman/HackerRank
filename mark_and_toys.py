# https://www.hackerrank.com/challenges/mark-and-toys
N,K = input().split()
N,K = int(N), int(K)
lst = list(map(int, input().split()))
lst = sorted(lst)
total = 0
required = 0
for i in range(len(lst)):
    if total < K and total + lst[i] <= K :
        total = total + lst[i]
        required += 1
    else:
        break
print(required)
