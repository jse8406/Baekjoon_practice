import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j)) # blank에 0값의 위치 (x,y좌표) 저장

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False # 가로줄 체크
    return True

def checkCol(y, a): # 세로줄 체크
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a): # a가 포홤되어있는 3x3 정사각형 체크 
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(a):
    if a == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[a][0]
        y = blank[a][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(a+1)
            graph[x][y] = 0

dfs(0)

# dfs(0)
# 문제없이 잘
# dfs(1)
# ..
# dfs(2)
# 모순 발생 => dfs(2)는 아무 실행 없이 끝 
# dfs(1) 에서 확정지은 값을 0으로 바꾸고 돌던 for 반복문 마저 돌기 시작
# 후보해가 여러개였다면 다른 후보를 대입하고 dfs(2)를 다시 실행하겠지만
# 후보해가 1개였다면 dfs(0)에서부터 모순이었으므로 하나더 거슬러 올라감
