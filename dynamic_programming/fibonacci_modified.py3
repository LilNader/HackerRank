t1, t2, n = [int(x) for x in input().split()]
dic = {1: t1, 2: t2}

def fib(n):
    if n in dic:
        return dic[n]
    dic[n] = fib(n-2) + pow(fib(n-1), 2)
    return dic[n]

print(fib(n))