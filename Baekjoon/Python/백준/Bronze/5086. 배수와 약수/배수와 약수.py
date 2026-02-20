import sys

ls = list()
while [0, 0] not in ls :
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    ls.append(a)
    if a[0] and a[1] != 0:
        if a[1] % a[0] == 0:
            print('factor')
            continue
        elif a[0] % a[1] == 0:
            print("multiple")
            continue
        else:
            print("neither")
            continue