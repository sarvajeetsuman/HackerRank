#!/usr/bin/py
# https://www.hackerrank.com/challenges/lonely-integer
# Head ends here
def lonelyinteger(b):
    answer = 0
    b =list(b)
    for i in range(len(b)):
        if b.count(b[i]) == 1:
            answer = b[i]
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))

