k, n = map(int,input().split())
cable = []
for _ in range(k):
    cable.append(int(input()))
min, max = 1, max(cable)
result = 0
while min <= max:
    mid = (min + max) // 2
    cable_nums = 0
    for i in cable:
        cable_nums += i // mid
    if cable_nums >= n:
        min = mid + 1
        result = mid
    else:
        max = mid - 1
print(result)