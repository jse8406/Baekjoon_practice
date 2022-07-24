def check(x):
    for i in range(x):
        if col[i] == col[x] or abs(col[x]-col[i]) == x - i:
            return False
    return True
def findqueen(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            findqueen(x+1)
cnt = 0
n = int(input())
col = [0]*n
findqueen(0)
print(cnt)
