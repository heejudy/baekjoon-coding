import sys 

input = sys.stdin.readline
lst = [0] * 10001

for i in range(int(input())):
    lst[int(input())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
    else:
        continue