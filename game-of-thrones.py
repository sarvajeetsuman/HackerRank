# https://www.hackerrank.com/challenges/game-of-thrones

count_dict = {}
count_of_odd = True
string = input()
length = len(string)
flag = True
for i in range(length):
    if string[i] in count_dict:
        count_dict[string[i]] = count_dict[string[i]] + 1
    else:
        count_dict[string[i]] = 1
if length%2 ==0:
    for key, value in count_dict.items():
        if value % 2 != 0:
            flag = False
            break
else:
    for key, value in count_dict.items():
        if value % 2 != 0:
            if count_of_odd == True:
                count_of_odd = False
                continue
            else:
                flag = False
                break
if flag == True:
    print('YES')
else:
    print('NO')
