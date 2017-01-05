# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

i,j,k = input().strip().split()
i,j,k = int(i), int(j), int(k)
count = 0
for num in range(i,j+1):
    rev = int(str(num)[::-1])
    if (num-rev)%k == 0:
        count += 1
print(count)
