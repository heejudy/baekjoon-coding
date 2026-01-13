from itertools import combinations 

N, M = list(map(int, input().split()))
a = list(map(int, input().split()))

result = 0

ls = list(combinations(a, 3))
for i in ls:
    s = sum(i)
    if s <= M and s > result:
        result = s

print(result)