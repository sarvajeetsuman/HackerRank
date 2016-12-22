# https://www.hackerrank.com/challenges/introduction-to-regex

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
num = int(input())
for i in range(num):
    f = raw_input()
    if re.match(r'\+',f) or re.match(r'\-',f) or re.match(r'\.',f) or re.match(r'[0-9]',f):
        if re.search('\.',f):
            if f.count('.') == 1:
                try:
                    num = float(f)
                    print True
                except ValueError:
                    print False
            else:
                print False
        else:
            print False
    else:
        print False
