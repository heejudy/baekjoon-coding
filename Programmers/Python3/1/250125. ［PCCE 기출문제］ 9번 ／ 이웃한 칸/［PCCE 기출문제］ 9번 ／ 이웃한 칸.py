def solution(board, h, w):
    cur_color = board[h][w]
    count = 0
    
    lst = [[h, w-1], [h-1, w], [h, w+1], [h+1, w]]
    
    for i in lst:
        if 0 <= i[0] < len(board) and 0 <= i[1] < len(board[0]):
            if board[i[0]][i[1]] == cur_color:
                count += 1
    
    return count