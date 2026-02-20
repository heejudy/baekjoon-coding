import sys

vy = list()
M = list()
a = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(a[0]):
    vy.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
for __ in range(a[1]):
    M.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

cumulative = [[0] * (a[0] + 1) for _ in range(a[0] + 1)]
for i in range(1, a[0] + 1):
    for j in range(1, a[0] + 1):
        cumulative[i][j] = vy[i - 1][j - 1] + cumulative[i - 1][j] + cumulative[i][j - 1] - cumulative[i - 1][j - 1]

for i in M:
    x1, y1, x2, y2 = i
    a = cumulative[x2][y2] - cumulative[x1 - 1][y2] - cumulative[x2][y1 - 1] + cumulative[x1 - 1][y1 - 1]
    print(a)
