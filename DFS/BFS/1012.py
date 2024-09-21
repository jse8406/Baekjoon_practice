import sys
sys.setrecursionlimit(100000)

def dfs(list, i,j):

    if j < len(list) and i <len(list[0]) and list[j][i] == 1:
        list[j][i] = -1
        if i-1 >=0:
            dfs(list, i-1, j)
        if i+1 < len(list[0]):
            dfs(list, i+1, j)
        if j-1 >=0:
            dfs(list, i, j-1)
        if j+1 < len(list):
            dfs(list, i, j+1)

num = int(input())



for _ in range(num):
    m,n,k = map(int,input().split())
    visited = [[0]*m for _ in range(n)]
    counter = 0
    for _ in range(k):
        i,j = map(int, input().split())
        visited[j][i] = 1 #배추가 심어져있는 위치
    for x in range(m):
        for y in range(n):
            if visited[y][x] == 1:
                counter += 1
                dfs(visited, x, y)
    print(counter) 
        

