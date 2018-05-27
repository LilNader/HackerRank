# Recursive Digit Sum
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def sum_digits(s):
    if len(s) == 1:
        return int(s)
    return sum_digits(str(sum([int(x) for x in s])))

n, k = input().split()
print(sum_digits(str(sum_digits(n)*int(k))))