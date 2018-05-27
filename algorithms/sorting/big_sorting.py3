# Big Sorting
# https://www.hackerrank.com/challenges/big-sorting/problem

n = int(input())
l = []
for _ in range(n):
    l.append(input())
# I dont know how, (well actually I do) but if you use the `int` function
# as the key, will perform the necessary operations (if needed) and won't
# convert the data type if it's not necessary.
# Fuck logic python
l.sort(key=int)
for x in l:
    print(x)