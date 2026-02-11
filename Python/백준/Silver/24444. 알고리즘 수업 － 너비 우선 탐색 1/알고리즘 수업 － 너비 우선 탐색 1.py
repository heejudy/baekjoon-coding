from collections import deque
import sys
input = sys.stdin.readline

node, edge, root = list(map(int, input().split()))
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    start, end = list(map(int, input().split()))
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)

for i in range(node):
    graph[i].sort()

result = [0 for i in range(node)]
que = deque()
que.append(root - 1)
visited = [False] * node

visited[root - 1] = True

count = 1
while que:
    u = que.popleft()
    result[u] = count

    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            que.append(v)
    count += 1
            
for i in result:
    print(i)