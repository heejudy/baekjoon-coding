import sys

a = int(input())
ls = []

for _ in range(a):
    b = sys.stdin.readline().rstrip()
    if 'push' in b.split(' '):
        ls.append(int(b.split()[-1]))
    if b == "top":
        if len(ls) == 0 :
            print(-1)
        else:
            print(ls[-1])
    if b == "size":
        print(len(ls))
    if b == 'empty':
        if len(ls) == 0:
            print(1)    
        else:
            print(0)    
    if b == 'pop':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[-1])
            ls.pop(-1)