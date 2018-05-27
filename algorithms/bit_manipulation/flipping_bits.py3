# Flipping bits
# https://www.hackerrank.com/challenges/flipping-bits/problem

t = int(input())
for _ in range(t):
    n = int(input())
    print(((1<<32)-1)^n)
