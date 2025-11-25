node = int(input())
edge = int(input())

graph = [[] for _ in range(node)]
for _ in range(edge):
    A, B = list(map(int, input().split()))
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

i = 0
visited_check = [False] * node

visited_check[i] = True
st = [i]

while len(st) != 0:
    u = st.pop()

    for v in graph[u]:
        if not visited_check[v]:
            visited_check[v] = True
            st.append(v)

print(visited_check.count(True)-1)