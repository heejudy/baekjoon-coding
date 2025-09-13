a = int(input())
b = list(map(int, input().split()))

s = set()
ls = list()
for i in b:
    for j in range(1, i+1):
        if i % j == 0:
            ls.append(j)
            ls.sort()
    if len(ls) == 2 and ls == [1, i]:
        s.add(i)
        ls = list()
    else:
        ls = list()
print(len(s))