# K Factorization
# https://www.hackerrank.com/challenges/k-factorization/problem
#
# Technique used: Backtracking.
# This problem trigger me a headache because in principle I didn't pruned
# the backtracking tree and started to calculate surplus cases and I
# didn't know how to prune it correctly.

solution = []

def compare_and_add_to_solution(s):
    global solution
    if not solution:
        solution = s
    if len(s) < len(solution):
        solution = s
    elif len(s) == len(solution):
        solution = sorted([solution, s])[0]

def factorization(n, k, xs, states, i=0):
    if states[-1] == n:
        return states
    elif states[-1] > n:
        return []
    else:
        while i < len(xs):
            a = states[-1] * xs[i]
            if a <= n:
                l = factorization(n, k, xs, states + [a], i)
                # Exists a solution.
                if len(l) > 0:
                    compare_and_add_to_solution(l)
            else:
                # Not explore the other k-i nodes.
                break
            i += 1
        return solution

n, k = [int(x) for x in input().split()]
xs = [int(x) for x in input().split()]
xs.sort()

r = factorization(n, k, xs, [1])
print(-1 if len(r) == 0 else ' '.join(str(x) for x in r))