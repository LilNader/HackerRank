# Permuting Two Arrays
# https://www.hackerrank.com/challenges/two-arrays/problem

def is_possible(a, b, n, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        if a[i] + b[i] < k:
            return 'NO'
    return 'YES'

q = int(input())
for _ in range(q):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(is_possible(a, b, n,  k))