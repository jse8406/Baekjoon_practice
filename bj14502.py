import copy
n,m = map(int, input().split())


answer = 0
virus_map = []

def spread(vm,i,j):
    n = len(vm)
    m = len(vm[0])
    vm[i][j] = 2
    #상
    if i-1>=0 and vm[i-1][j] == 0:
        spread(vm,i-1, j)
    #하
    if i+1<n and vm[i+1][j] == 0:
        spread(vm,i+1,j)
    #좌
    if j-1>=0 and vm[i][j-1] == 0:
       spread(vm, i, j-1)
    #우
    if j+1 <m and vm[i][j+1] == 0:
        spread(vm, i, j+1) 
    


for i in range(n):
    virus_map.append(list(map(int, input().split())))


clone = copy.deepcopy(virus_map)
answer = []
virus_pos = []
block_num = 3

for i in range(n):
    for j in range(m):
        if virus_map[i][j] == 2:
            virus_pos.append([i,j])

count = 0

# 벽을 세우고 spread 후 안전지대 

for i in range(n):
    for j in range(m):
        if clone[i][j] == 0:
            clone[j][j] = 1
            
print(max(answer))
print(answer)