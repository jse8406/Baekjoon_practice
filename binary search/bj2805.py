n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

answer = 0
while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in trees:
        if i - mid > 0:
            sum += i - mid
    if sum >= m: #나무가 남는다
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)