## 방문하지 않았으면서 입력이 1인 곳을 BFS로 탐색, 그때마다 answer을 1씩 증가
N = int(input())

houses = []
for _ in range(N):
    houses.append(input())
    # str로 받아도 indexing 가능

answer = 0

dx = [1, -1, 0, 0]
dy = [0 ,0 ,1, -1]

visited = [[0]*N for _ in range(N)]
# 재귀말고 deque로도 짤 수 있음. 다음에 방문해야하는 점을 queue에 넣어서 반복.
def BFS(i,j):
    num_house = 1
    visited[i][j] = 1
    # dx, dy는 위에 배열에서 인덱스 짝이 맞도록 움직여야만 상하좌우로만 움직인다.
    # 만약 이중 포문으로 dx, dy를 다 순회하면 대각선까지 움직일 수 있게된다. 만약 그렇게 움직일 수 있다면 그렇게 하면 된다.
    for k in range(4):
        x = dx[k] + i
        y = dy[k] + j
        if 0 <= x <N and 0 <= y <N:
            # num_house는 지역 변수라 누적합이 정상적으로 잘 된다.
            if not visited[x][y] and houses[x][y] == '1':
                num_house += BFS(x,y)
    return num_house
count = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and houses[i][j] == '1':
            answer += 1
            c = BFS(i,j)
            count.append(c)
print(answer)
for c in count:
    print(c)




