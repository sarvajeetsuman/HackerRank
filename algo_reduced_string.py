# https://www.hackerrank.com/challenges/reduced-string
ini_str = input()
itr = 0
curr_length = len(ini_str) - 1
i=0
while(i<curr_length):
    if ini_str[itr] == ini_str[itr+1]:
        ini_str = ini_str[:itr]+ini_str[itr+2:]
        itr = 0
        i=0
        curr_length = len(ini_str)-1
        if curr_length <= 0:
            break
        else:
            continue
    else:
        i=i+1
        itr = itr +1
        if len(ini_str) >2:
            continue
        else:
            break
if len(ini_str)>0 :
    print(ini_str)
else:
    print("Empty String")
