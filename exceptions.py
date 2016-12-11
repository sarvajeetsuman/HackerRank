# https://www.hackerrank.com/challenges/exceptions

n = int(input())
for i in range(n):
    lst = list(input().split())
    try:
        print(int(int(lst[0])/int(lst[1])))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
