import sys
input = sys.stdin.readline

N = int(input())
ls = []
for _ in range(N):
    a, b = input().split(' ')
    ls.append([int(a), b.strip()])

ls.sort(key=lambda x : x[0])
for i in ls:
    print(str(i[0]) + " " + i[1])