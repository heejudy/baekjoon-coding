import sys
input = sys.stdin.readline

N = int(input())  

result = []
for i in range(N):
    a = input().strip()
    if a in result:
        continue
    else:
        result.append(a)

result.sort(key=lambda x: (len(x), x))

for i in result:
    print(i)