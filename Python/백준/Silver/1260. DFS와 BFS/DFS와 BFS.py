import sys
from collections import deque
input = sys.stdin.readline

node, edge, root = list(map(int, input().split()))

graph = [[] for _ in range(node)]

for _ in range(edge):
    start, end = list(map(int, input().split()))
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)

for i in range(node):
    graph[i].sort(reverse=True)


# DFS
root -= 1

DFS_list = []
st = [root]
visited = [False] * node

while st:
    u = st.pop()

    if not visited[u]:
        visited[u] = True
        DFS_list.append(u + 1)

        for v in (graph[u]):
            if not visited[v]:
                st.append(v)
            
for i in DFS_list: 
    print(i, end = " ")
print()

# BFS
BFS_list = []
st = deque()
st.append(root)
visited = [False] * node

visited[root] = True

while st:
    u = st.popleft()
    BFS_list.append(u + 1)

    for v in reversed(graph[u]):
        if not visited[v]:
            visited[v] = True
            st.append(v)

for i in BFS_list:
    print(i, end = " ")