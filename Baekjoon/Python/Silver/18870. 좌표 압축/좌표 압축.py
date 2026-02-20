import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

d = dict()
lst1 = list(set(lst.copy()))
lst1.sort()

for key, value in enumerate(lst1):
    d[value] = key

for i in lst:
    print(d.get(i), end = " ")