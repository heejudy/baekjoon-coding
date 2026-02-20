N, M = map(int, input().split())

a = []
for i in range(N):
    a.append(input().split())

b = [] 
for i in range(N):
    b.append(input().split())

for i in range(0,N):
    for j in range(0,M):
        print(int(a[i][j]) + int(b[i][j]), end=' ')
    print()