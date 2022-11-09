N = int(input())
board = []

for _ in range(N):
  l = list(map(int, input().split()))
  board.append(l)
white_0 = 0
blue_1 = 0

def solution(x,y,N):
  global white_0
  global blue_1
  color = board[x][y]
  for i in range(x,x+N):
    for j in range(y,y+N):
      if color != board[i][j]:
        solution(x,y,N//2)
        solution(x+N//2,y,N//2)
        solution(x,y+N//2,N//2) 
        solution(x+N//2,y+N//2,N//2)
        return
  if color == 0:
    white_0 += 1
  else:
    blue_1 += 1

solution(0,0,N)

print(white_0)
print(blue_1)