# https://www.hackerrank.com/challenges/flipping-bits
t = int(input())
for i in range(t):
    num = int(input())
    binary = '{0:032b}'.format(num)
    binary_list = []
    binary_list = list(binary)
    for i in range(32):
        if int(binary_list[i]) == 0:
            binary_list[i] = '1'
        else:
            binary_list[i] = '0'
    new_binary = ''.join(binary_list)
    print(int(new_binary, 2))
