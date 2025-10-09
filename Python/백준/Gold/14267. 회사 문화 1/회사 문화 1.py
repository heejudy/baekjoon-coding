import sys
input = sys.stdin.readline 

n, m = map(int, input().split()) 

parent = [0] + list(map(int, input().split()))
count = [0] * (n+1)

for i in range(m):
    u, cnt = map(int, input().split())
    count[u] += cnt

for i in range(2, n+1):
    count[i] += count[parent[i]]

for i in range(1, len(count)):
    print(count[i], end = ' ')