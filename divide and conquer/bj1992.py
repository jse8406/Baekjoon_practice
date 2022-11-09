N = int(input())
board = []

for _ in range(N):
  l = list(map(int, input()))
  board.append(l)
result = ''

def solution(x,y,N):
  global result
  color = board[x][y]
  for i in range(x,x+N):
    for j in range(y,y+N):
      if color != board[i][j]:
        result += '('
        solution(x,y,N//2)
        solution(x,y+N//2,N//2) 
        solution(x+N//2,y,N//2)
        solution(x+N//2,y+N//2,N//2)
        result += ')'
        return
  if color == 0:
    result += str(0)
  else:
    result += str(1)


solution(0,0,N)
print(result)