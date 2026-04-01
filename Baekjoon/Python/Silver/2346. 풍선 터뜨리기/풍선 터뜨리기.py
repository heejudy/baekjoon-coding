from collections import deque

n = int(input())
arr = list(map(int, input().split()))
dq = deque()

for i in range(n):
    dq.append((i + 1, arr[i]))

answer = []

while dq:
    ind, move = dq.popleft()
    answer.append(ind)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move - 1))  
    else:
        dq.rotate(-move)        

print(*answer)