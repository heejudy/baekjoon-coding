N = int(input())

day_lst = []
money_lst = []

for i in range(N):
    a, b = list(map(int, input().split()))
    day_lst.append(a)
    money_lst.append(b)

DP = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + day_lst[i] <= N:
        DP[i] = max(DP[i+1], money_lst[i] + DP[i + day_lst[i]])
    else:
        DP[i] = DP[i+1]

print(DP[0])