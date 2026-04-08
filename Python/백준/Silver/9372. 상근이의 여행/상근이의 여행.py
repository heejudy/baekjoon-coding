from collections import deque

T = int(input())

for _ in range(T):
    nation, airplane = list(map(int, input().split()))
    graph = [[] for i in range(nation+1)]
    visited = [0 for i in range(nation+1)]
    for i in range(airplane): 
        a, b = list(map(int, input().split()))
        # 그래프 생성하기
        graph[a] += [b]
        graph[b] += [a]

    cnt = 0
    visited[1] = 1
    dq = deque([1])
    while dq:
        u = dq.popleft()
        cnt += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = 1
                dq.append(v)

    print(cnt - 1)