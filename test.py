n = int(input())
area = [list(input()) for _ in range(n)]
B_position = []
for i in range(n): # R and G are same
  for j in range(i):
    if(area[i][j]) == 'B':
      B_position.append([i,j])
print(B_position)
  