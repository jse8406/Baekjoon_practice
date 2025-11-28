def win(board, t):
    # 가로 
    for b in board:
        if b == t*3:
            return True
    # 세로
    for i in range(3):
        if board[0][i] == t and board[1][i] == t and board[2][i] == t:
            return True
    # 대각
    if board[0][0] == board[1][1] == board[2][2] == t:
        return True
    if board[2][0] == board[1][1] == board[0][2] == t:
        return True
    return False

def solution(board):
    o_cnt, x_cnt = 0,0
    for b in board:
        for c in b:
            if c == "O":
                o_cnt +=1
            elif c == "X":
                x_cnt +=1
    if not (o_cnt == x_cnt or o_cnt==x_cnt+1):
        return 0
    if win(board, "X") and win(board, "O"):
        return 0
    if win(board,"X") and o_cnt != x_cnt:
        return 0
    if win(board, "O") and o_cnt != x_cnt +1:
        return 0
                
    return 1