import sys
input = sys.stdin.readline

node, edge, root = list(map(int, input().split()))

graph = [[] for _ in range(node)]

for _ in range(edge):
    start, end = list(map(int, input().split()))
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)

for i in graph:
    i.sort(reverse=True)

DFS_list = [0 for i in range(node)]
stack = [root - 1]
visited = [False] * node

count = 1
while stack:
    u = stack.pop()

    if not visited[u]:
        visited[u] = True
        DFS_list[u] = count 
        count += 1

    for v in graph[u]:
        if not visited[v]:
            stack.append(v)
    
        
for i in DFS_list:
    print(i)