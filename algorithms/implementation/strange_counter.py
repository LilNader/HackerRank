# Strange Counter
# https://www.hackerrank.com/challenges/strange-code/problem

n = int(input())
max_score = 10e12

a, b = 1, 3
t_v_l = []
r = 0

while b < max_score:
    t_v_l.append((a, b,))
    a += b
    b *= 2

for i in range(len(t_v_l)):
    if(t_v_l[i][0] <= n):
        r = t_v_l[i][1] - (n - t_v_l[i][0])

print(r)