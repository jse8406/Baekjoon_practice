n = int(input())
ans = 1
dance = ["ChongChong"]
for i in range(n):
    first, second = input().split(" ")
    if (first in dance and second not in dance):
        ans += 1
        dance.append(second)
    elif (first not in dance and second in dance):
        ans += 1
        dance.append(first)
print(ans)

# set 자료구조를 사용하면 조건문의 조건을 더 간결하게 줄일 수 있다.