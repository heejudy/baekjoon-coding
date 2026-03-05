def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
            else:
                continue
    
    answer = 0
    for i in board:
        answer = max(answer, max(i))

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer ** 2