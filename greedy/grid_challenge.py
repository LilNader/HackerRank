def foo(m):
    n = len(m)
    m_aux = []
    for x in m:
        m_aux.append(sorted(x))
    for i in range(n):
        for j in range(n-1):
            if ord(m_aux[j][i]) > ord(m_aux[j+1][i]):
                return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    m = []
    for _ in range(n):
        m.append([x for x in input()])
    print(foo(m))