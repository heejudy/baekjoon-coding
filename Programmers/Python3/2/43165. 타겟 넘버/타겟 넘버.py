def solution(numbers, target):
    answer = 0
    # 문제 풀이 방법 
    # 트리를 만들어 나가는데 왼쪽 노드는 -, 오른쪽 노드는 + 해줌 
        # 전체적으로 탐색해야 하기 때문에 dfs 사용
        # 현재 index와 현재까지 계산된 값을 넘겨줌 
    # 트리의 깊이가 numbers의 길이가 되었을 때 target과 일치하는지 확인함 
    
     
    def dfs(index, total):     
        nonlocal answer
        # 도달 시 target과 동일하다면 answer += 1
        if index == len(numbers):
            if total == target:
                answer += 1
            return 
        
        dfs(index + 1, total - numbers[index])
        dfs(index + 1, total + numbers[index])
        
        
    dfs(0, 0)
        
    return answer