import sys
a = []
for i in range(int(sys.stdin.readline().rstrip())):
    a.append(int(sys.stdin.readline().rstrip()))  
for i in sorted(a):
    print(i)