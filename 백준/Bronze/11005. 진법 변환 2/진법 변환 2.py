from collections import deque
import sys
input = sys.stdin.readline


N, B = list(map(int, input().split()))

result = deque()

while (N >= B):
    result.appendleft(N % B)
    N = int(N / B)
result.appendleft(N)

answer = ""
for i in result:
    if i >= 10: 
        answer += chr(i + 55)
    else:
        answer += str(i)
print(answer)