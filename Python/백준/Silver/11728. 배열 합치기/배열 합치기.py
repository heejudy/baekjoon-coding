import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = []
first = list(map(int, input().split()))
second = list(map(int, input().split()))

i, j = 0, 0
while (i < len(first) and j < len(second)):
    if first[i] < second[j]:
        total.append(first[i])
        i += 1
    else: 
        total.append(second[j])
        j += 1
if (i <= len(first)):
    total.extend(first[i:len(first)])
if (j <= len(second)):
    total.extend(second[j:len(second)])

for i in total:
    print(i)