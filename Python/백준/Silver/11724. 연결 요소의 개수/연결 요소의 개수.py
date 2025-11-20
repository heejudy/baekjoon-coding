import sys
from collections import deque

input = sys.stdin.readline

node, edge = list(map(int, input().split()))

l = [[] for _ in range(node)]

for i in range(edge):
    u, v = list(map(int, input().split()))
    l[u-1].append(v-1)
    l[v-1].append(u-1)


visit = [False] * node
count = 0

for i in range(node):
    if visit[i]:
        continue

    count += 1

    d = deque([i])
    visit[i] = True

    while len(d) != 0:
        u = d.popleft()

        for v in l[u]:
            if not visit[v]:
                d.append(v)
                visit[v] = True

print(count)