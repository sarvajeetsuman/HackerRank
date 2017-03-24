# https://www.hackerrank.com/challenges/funny-string
t = int(input())
for i in range(t):
    string = input()
    flag = True
    n = len(string)
    if n%2 == 0:
        for i in range((n//2)-1):
            if abs(ord(string[i])- ord(string[i+1])) != abs(ord(string[n-i-1])-ord(string[n-i-2])):
                flag = False
                break
    else:
        for i in range((n//2)):
            if abs(ord(string[i])- ord(string[i+1])) != abs(ord(string[n-i-1])-ord(string[n-i-2])):
                flag = False
                break
        
    if flag == False:
        print('Not Funny')
    else:
        print('Funny')
