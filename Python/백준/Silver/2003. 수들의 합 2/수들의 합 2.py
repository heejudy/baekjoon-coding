import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

j = 0
i = 0
result = 0
while i != (N) and j!= (N):
    if sum(num_list[i:j+1]) < M:
        j += 1
    elif sum(num_list[i:j+1]) > M:
        i += 1
        j = i
    else:
        result += 1
        i += 1
        j = i

print(result)