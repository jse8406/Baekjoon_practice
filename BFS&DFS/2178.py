N, M = map(int, input().split())

miro = []

for _ in range(N):
    miro.append(input())
distance = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

distance[0][0] = 1
visited[0][0] = 1

from collections import deque
q = deque()
q.append([0,0])

while q:
    x,y = q.popleft()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 범위 안에 있고, 미로갈 수 있는 길이고, 방문안하면 갈 수 있음
        # 아예 못들어가는데 지금 ? 
        if 0<=nx<N and 0<=ny<M and miro[nx][ny] == '1' and not visited[nx][ny]:
            distance[nx][ny] = distance[x][y] + 1
            visited[nx][ny] = 1
            q.append([nx,ny])


print(distance[N-1][M-1])


