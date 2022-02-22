def solution(board):
    answer = 0
    h = len(board)
    w = len(board[0])
    if (h < 2 or w < 2):
        return 1
    for x in range(1, h):
        for y in range(1, w):
            if board[x][y] == 1:
                board[x][y] =  1+min(board[x-1][y], board[x][y-1], board[x-1][y-1])
                answer = max(answer, board[x][y])
    return answer*answer