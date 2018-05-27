# The Power Sum
# https://www.hackerrank.com/challenges/the-power-sum/problem
# 
# This problem really took me a while to understand how to approach some 
# problems using backtracking technique. :^)

def possible_ways(x, n, nums):
    # Sum the numbers raised to n power.
    s = sum(map(lambda y: y**n, nums))

    # Base case
    if s == x:
        #print(nums) # Just for testing
        return 1
    else:
        # Take the last element of list if exist, otherwise will be 1
        last = 1 if len(nums) == 0 else nums[-1] + 1
        res = 0
        while s + last**n <= x:
            # Creating the recursion tree
            res += possible_ways(x, n, nums + [last])
            last += 1
        return res

x = int(input())
n = int(input())

print(possible_ways(x, n, []))