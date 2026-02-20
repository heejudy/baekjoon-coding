N = int(input())

level = []
for _ in range(N):
    level.append(int(input()))
level.reverse()

count = 0
for i in range(N-1):
    if level[i] <= level[i+1]:
        sub = level[i+1] - level[i] + 1
        count += sub
        level[i+1] -= sub

print(count)