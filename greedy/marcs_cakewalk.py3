n = int(input())
l = [int(x) for x in input().split()]
l.sort(reverse=True)
r = 0
for i in range(n):
    r += l[i] * (1<<i)
print(r)