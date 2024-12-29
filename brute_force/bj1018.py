N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())
for a in range(N-7):        #8x8 단위로 찍어서 한번씩 조사
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 첫 번째 칸부터 시작한 격자 무늬
                    if board[i][j] != 'W': # 맨 왼쪽 위 칸이 흰색인 경우
                        index1 += 1 # 바꿔야하는 판
                    if board[i][j] != 'B': # 맨 왼쪽 위 칸이 검은색인 경우
                        index2 += 1
                else: # 두 번째 칸부터 시작한 격자 무늬늬
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))