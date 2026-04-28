def solution(triangle):
    answer = 0
    
    depth = len(triangle)
    dp = [[0] * depth for i in range(depth)]
    
    for i in range(depth):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
    answer = max(dp[-1])
        
    
    return answer