import sys

a = list(map(int, sys.stdin.readline().rstrip().split()))
ls = list()
for i in range(1, a[0]+1):
    if a[0] % i == 0:
        ls.append(i)
ls.sort()
if len(ls) >= a[1]:
    print(list(ls)[a[1]-1])
else: 
    print(0)