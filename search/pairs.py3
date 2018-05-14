# Techinique used: bynary search.
# The idea was to sort the elements into an array (and removing duplicates),
# then do binary search for each element looking for the element plus k.

def binary_search(l, low, high, k):
    # Search through it recursivelly
    if high >= low:
        m = low + ((high - low)//2)
        if k == l[m]:
            return m
        elif k > l[m]:
            return binary_search(l, m+1, high, k)
        else:
            return binary_search(l, low, m-1, k)
    # Element not found
    return -1


def count_pairs(n, k, l):
    xs = sorted(set(l))
    res = 0
    for i in range(n-1):
        # Check if exist a pair with difference k
        if binary_search(xs, i+1, n-1, xs[i]+k) != -1:
            res += 1
    return res

#print(binary_search([1], 0, 1, 0))

n, k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
print(count_pairs(n, k, l))