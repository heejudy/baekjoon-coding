def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    graph = [[] for _ in range(n)]
    
    def dfs(start, target, visited):
        if start == target:
            return True
        
        visited[start] = True
        
        for next_node in graph[start]:
            if not visited[next_node]:
                if dfs(next_node, target, visited):
                    return True
        
        return False
    
    for i in range(len(costs)):
        a = costs[i][0]
        b = costs[i][1]
        cost = costs[i][2]
        
        visited = [False] * n
        
        if not dfs(a, b, visited): 
            graph[a].append(b)
            graph[b].append(a)
            answer += cost
    
    return answer