l = int(input())
r = int(input())
max_ = -1

for a in range(l, r+1):
    for b in range(a, r+1):
        aux = a^b
        if aux > max_:
            max_ = aux

print(max_)