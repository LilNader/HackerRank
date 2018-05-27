# Minimum Absolute Difference in an Array
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

n= int(input())
l = [int(x) for x in input().split()]
l.sort()
min_ = abs(l[0] - l[1])
for i in range(n-1):
    aux = abs(l[i]-l[i+1])
    if aux == 0:
        min_ = 0
        break
    elif aux < min_:
        min_ = aux
print(min_)