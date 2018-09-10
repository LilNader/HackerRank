# Greedy Algorithms: Luck Balance
# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

n, k = [int(x) for x in input().split()]

wins = []
loses = []

for _ in range(n):
	a, b = [int(x) for x in input().split()]
	if b == 0:
		loses.append(a)
	elif b == 1:
		wins.append(a)

wins.sort(reverse=True)
loses.sort(reverse=True)

r = 0

i = 0
for i in range(len(wins)):
	if i < k:
		r += wins[i]
	else:
		r -= wins[i]
	i += 1

print(r + sum(loses))
