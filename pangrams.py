array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

string = input().strip().lower()
flag = True

for element in array:
    try:
        ind=string.index(element)
    except:
        ind = -1
    if ind<=-1:
        flag = False
        break
if flag==False:
    print("not pangram")
else:
    print("pangram")
