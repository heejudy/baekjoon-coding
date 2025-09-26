N = int(input())
M = sorted(list(map(int, input().split())))

total = 0
for i in range(N):
    total += sum(M[0:i+1])

print(total)