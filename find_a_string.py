# https://www.hackerrank.com/challenges/find-a-string

string =input()
substring = input()
count = 0
i=0
while(i<(len(string)-len(substring))):
    if(string.find(substring,i,len(string))>=0):
        count+=1
        i=string.find(substring,i,len(string))+1
    else:
        break;
print(count)
