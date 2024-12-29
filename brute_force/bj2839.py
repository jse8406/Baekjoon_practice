# 입력 설탕 무게를 5로 나눈 몫 x에서 1식 빼면서 3으로 나눠 떨어질 때까지 반복, 안되면 -1, 되면 5의 몫과 3의 몫 합 출력
# 5로 나눠 떨어질 때 까지 3을 빼면서 반복....
n = int(input())

share = n//5
remainder = n%5

while share >= -1:
    if share == -1:
        print(share)
        break
    elif remainder % 3 == 0:
        r = remainder // 3
        print(share+r)
        break
    else :
        share -= 1
        remainder += 5