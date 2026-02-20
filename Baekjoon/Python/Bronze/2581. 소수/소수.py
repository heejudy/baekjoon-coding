M = int(input())
N = int(input())

ls = list()
s = list()
for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            ls.append(j)
            ls.sort()
    if len(ls) == 2 and ls == [1, i]:
        s.append(i)
        ls.clear()
    else:
        ls.clear()
if len(s) > 0:
    print(sum(s))
    print(min(s))
else: 
    print(-1)