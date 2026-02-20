n = int(input())
dp = [[0]*n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if i == 0:
            dp[i][j] = row[j]
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] + row[j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + row[j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + row[j]

print(max(dp[n-1]))
