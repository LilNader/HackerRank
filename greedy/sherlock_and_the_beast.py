def foo(n):
    s = ''.join(['5' for _ in range(n)])
    n_5, n_3 = n, 0
    for _ in range(n+1):
        if n_5%3 == 0 and n_3%5 == 0:
            return s + '3'*n_3
        else:
            s = s[:-1]
            n_5 -= 1
            n_3 += 1
    return -1


t = int(input())
for _ in range(t):
    print(foo(int(input())))