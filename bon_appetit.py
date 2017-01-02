# https://www.hackerrank.com/challenges/bon-appetit
n,k = input().split()
n,k = int(n), int(k)
plst = [int(i) for i in input().strip().split()]
charged = int(input())
total_price_of_shared_items = sum(plst)-plst[k]
each_share = total_price_of_shared_items//2
if each_share == charged:
    print("Bon Appetit")
else:
    print(charged-each_share)


