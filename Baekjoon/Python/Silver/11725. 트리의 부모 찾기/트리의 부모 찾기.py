#4
node = int(input())

graph= [[] for _ in range(node)]
for _ in range(node-1):
    A, B = list(map(int, input().split()))
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

lis = [0 for _ in range(node)]
count = 0
i = 0
visited_check = [False] * node

st = [i]
visited_check[i] = True

while len(st) != 0:
    u = st.pop()  

    for v in graph[u]:
        if not visited_check[v]:
            lis[v] = u + 1
            visited_check[v] = True
            st.append(v)


lis.pop(lis[0])
for i in lis:
    print(i)