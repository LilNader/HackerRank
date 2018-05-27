# Lonely Integer
# https://www.hackerrank.com/challenges/lonely-integer/problem

# The idea is to use the XOR properties, the logical operation satifies
# commutativity, and associasivity.
# Since it can commute and associate, if two numbers are the same then a^a=0,
# and we can pair any two elements (without loss of generality) and of
# every pair we'll have a 0 as a result, and now we'are interested in a element
# which hasn't been paired, so if we have (a_1^a_2)^...^(a_n^a_n)=0.
# 0^b_k= b_k. Thus (a_1^a_2)^...^(a_n^a_n)^(b_k)=0^b_k=b_k

t = int(input())
l = [int(x) for x in input().split()]
r = 0
for x in l:
    r ^= x
print(r)