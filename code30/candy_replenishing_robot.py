import sys
n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
c = list(map(int, input().strip().split(' ')))

candy_left = 0
temp = n
req = 0
for i in range(t-1):
	candy_left = temp - c[i]
	if candy_left < 5:
		req = req + n - candy_left
		temp = n
	else :
		temp = temp - c[i]
print(req)

