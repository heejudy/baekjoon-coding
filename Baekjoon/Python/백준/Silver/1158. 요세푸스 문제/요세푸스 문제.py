from collections import deque
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
dq = deque([i for i in range(1, n + 1)])
result = [] 

while len(dq) != 0:
    dq.rotate(-(k-1))
    result.append(dq.popleft())

print('<' + ', '.join(map(str, result)) + '>')