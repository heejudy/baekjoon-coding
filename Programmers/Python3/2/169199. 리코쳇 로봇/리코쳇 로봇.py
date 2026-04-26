from collections import deque

def solution(board):
    answer = 0
    
    board_list = [list(row) for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board_list[i][j] == 'R':
                start = [i, j]
    
    # BFS 초기 설정 
    # 방문 확인 
    M = len(board)
    N = len(board[0])
    visited = [[False] * N for i in range(M)]

    dq = deque() 
    
    visited[start[0]][start[1]] = True
    dq.append((start[0], start[1], 0))
    
    while dq:
        x, y, cnt = dq.popleft()
        
        if board[x][y] == 'G':
            return cnt 
        
        # 위 오 아 왼
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x, y
            
            while True:
                cx, cy = nx + dx, ny + dy
                
                if not (0 <= cx < M and 0 <= cy < N):
                    break
                if board_list[cx][cy] == 'D':
                    break
                
                nx, ny = cx, cy
                
            if nx == x and ny == y:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt + 1))
                
    if board[nx][ny] != 'G':
        return -1
    
    return answer