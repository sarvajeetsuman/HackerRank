# https://www.hackerrank.com/challenges/designer-pdf-viewer

#!/bin/python3

import sys


h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

wordlst = list(word)
charcount = len(wordlst)
valuelst = []

for char in wordlst:
    valuelst.append(h[alphabet.index(char)])

print(max(valuelst)*charcount)

