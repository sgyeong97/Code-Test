def solution(board, moves):
    answer = 0
    basket = [0]
    
    for x in moves:
        for y in range(len(board)):
            if board[y][x-1] != 0:
                doll = board[y][x-1]
                board[y][x-1] = 0
                break
            else:
                doll = -1
        if doll != -1:
            if basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)
    return answer