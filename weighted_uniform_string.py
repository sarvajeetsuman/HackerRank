#!/bin/python3

import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

sub_str = []
new_list = []
value_list = []


s = input().strip()
n = int(input().strip())
sub_str = get_all_substrings(s)
for element in sub_str:
    if len(set(element)) == 1:
        new_list.append(element)
        value = 0
        for i in range(len(element)):
            value = value + alphabet.index(element[i]) + 1
            value_list.append(value)
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    if x in value_list:
        print("Yes")
    else:
        print("No")
    
