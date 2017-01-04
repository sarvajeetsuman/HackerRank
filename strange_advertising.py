# https://www.hackerrank.com/challenges/strange-advertising

start = 5
no_of_days = int(input())
required_sum = 0
for i in range(no_of_days):
    if i == 0 :
        required_sum = start // 2
        spread = required_sum*3
    else:
        temp = spread//2
        required_sum = required_sum + temp
        spread = temp*3
print(required_sum)
