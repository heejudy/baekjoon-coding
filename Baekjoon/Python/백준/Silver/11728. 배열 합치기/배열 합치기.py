import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = []
first = list(map(int, input().split()))
second = list(map(int, input().split()))

i, j = 0, 0
while (i < a and j < b):
    if first[i] < second[j]:
        total.append(first[i])
        i += 1
    else: 
        total.append(second[j])
        j += 1
if (i <= a):
    total.extend(first[i:a])
if (j <= b):
    total.extend(second[j:b])

for i in total:
    print(i)