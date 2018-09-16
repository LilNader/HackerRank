def binary_search(l, e, left, right):
    if left > right:
        return None
    mid = left + (right-left)//2
    if l[mid][1] == e:
        return l[mid]
    elif l[mid][1] > e:
        return binary_search(l, e, left, mid-1)
    else:
        return binary_search(l, e, mid+1, right)

t = int(input())
for _ in range(t):
    money = int(input())
    n = int(input())
    l = [(i+1, int(x)) for i, x in enumerate(input().split())]
    #print(l)
    l.sort(key=lambda x: x[1])
    #print(l)
    for i in range(n):
        b = abs(money-l[i][1])
        r = binary_search(l, b, i+1, n-1)
        if r is not None:
            print(l[i][0], r[0])
