import sys

k = 0 
ls = [0]
a = map(int, sys.stdin.readline().rstrip().split())
b = list(map(int, sys.stdin.readline().rstrip().split()))
for i in b:
    k += i 
    ls.append(k)
for i in range(list(a)[1]):
    c = list(map(int, sys.stdin.readline().rstrip().split()))
    print(ls[c[1]]-ls[c[0]-1])