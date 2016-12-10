#https://www.hackerrank.com/challenges/py-set-add
n = int(input())
country = []
for i in range(n):
    country.append(input())
print(len(set(country)))
