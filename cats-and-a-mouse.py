# https://www.hackerrank.com/challenges/cats-and-a-mouse

#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if x > y:
        if z <= y:
            print('Cat B')
        elif z>=x:
            print('Cat A')
        elif y < z and x >z:
            if z-y > x-z:
                print('Cat A')
            elif z-y < x-z:
                print('Cat B')
            else:
                print('Mouse C')
    elif y > x:
        if z <= x:
            print('Cat A')
        elif z>=y:
            print('Cat B')
        elif x < z and y >z:
            if z-x > y-z:
                print('Cat B')
            elif z-x < y-z:
                print('Cat A')
            else:
                print('Mouse C')
    else:
        print('Mouse C')
