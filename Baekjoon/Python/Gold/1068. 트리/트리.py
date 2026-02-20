from sys import setrecursionlimit
setrecursionlimit(10**6)

N = int(input())
node_list = list(map(int, input().split()))
delete_node = int(input())

graph = [[] for i in range(N)]
root = -1

for i in range(N):
    parent = node_list[i]
    if parent == -1:
        root = i
        continue
    graph[i].append(parent)
    graph[parent].append(i)

def dfs(node):
    if node == delete_node:
        return 0
    
    child_count = 0
    leaf_count = 0

    for nxt in graph[node]:
        if nxt != delete_node and nxt != node_list[node]:
            leaf_count += dfs(nxt)
            child_count += 1

    if child_count == 0:
        return 1
    return leaf_count

if root == delete_node:
    print(0)
else:
    print(dfs(root))