# https://www.hackerrank.com/challenges/recursive-digit-sum
flag = True
def find_super_digit(p,k):
    global flag 
    lst = list(map(int,p))
    q = sum(lst)
    if flag == True:
        q = q*k
        flag = False
        
    if len(str(q)) == 1 :
        return q
    else:
        return find_super_digit(str(q),k)
n,k = input().split()
k = int(k)
p = n
super_digit = 0
super_digit = find_super_digit(p,k)
print(super_digit)


