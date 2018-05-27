# Intro to Tutorial Challenges
# https://www.hackerrank.com/challenges/tutorial-intro/problem

v = input()
n = int(input())
l = [x for x in input().split()]

for i in range(n):
    if v == l[i]:
        print(i)