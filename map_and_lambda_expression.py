cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
