N = int(input())
board = []

for _ in range(N):
  l = list(map(int, input().split()))
  board.append(l)

m1 = 0
zero = 0
p1 = 0

def solution(x,y,N):
  global m1, zero, p1
  paper = board[x][y]
  for i in range(x,x+N):
    for j in range(y,y+N):
      if paper != board[i][j]:
        solution(x, y, N//3)
        solution(x + N//3, y, N//3)
        solution(x + 2*N//3, y, N//3)
        
        solution(x, y + N//3 , N//3) 
        solution(x + N//3, y+ N//3 , N//3)
        solution(x + 2*N//3, y+ N//3 , N//3)
        
        solution(x, y + 2*N//3 , N//3) 
        solution(x + N//3, y + 2*N//3 , N//3)
        solution(x + 2*N//3, y + 2*N//3 , N//3)
        
        return
  if paper == -1:
    m1 += 1
  elif paper == 0:
    zero += 1
  else:
    p1 += 1

solution(0,0,N)

print(m1)
print(zero)
print(p1)