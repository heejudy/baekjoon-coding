import sys

a = int(sys.stdin.readline().rstrip())
a1 = set(map(int, sys.stdin.readline().rstrip().split()))
b = int(sys.stdin.readline().rstrip())
a2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in a2:
    if i in a1:
        print(1)
    else:
        print(0)