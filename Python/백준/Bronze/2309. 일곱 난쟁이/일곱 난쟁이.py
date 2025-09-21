from itertools import combinations

l = []
for _ in range(9):
    l.append(int(input()))

for i in list(combinations(l, 7)):
    if sum(i) == 100:
        for k in sorted(i):
            print(k)
        break 