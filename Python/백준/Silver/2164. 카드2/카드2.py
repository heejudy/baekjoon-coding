import sys
from collections import deque

N = int(input())
d = deque([])

for i in range(N):
    d.append(i+1)

while len(d) != 1:

    d.popleft()
    a = d.popleft()
    d.append(a)

print(d[0])