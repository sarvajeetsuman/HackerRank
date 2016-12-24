import re
str = input()
lst = re.split('\,',str)
for i in lst:
    if(i.find('.')!=-1):
        lst1 = re.split('\.',i)
        for e in lst1:
            if e !='':
                print (e)
    else:
        if i !='':
            print (i)
