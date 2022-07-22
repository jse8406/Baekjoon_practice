# 여기서 알수있는것이 먼저 8 7 6 5 4 2 1에서 2의 배수의 갯수를 구한다. 8/2 = 4
# 다음으로 제곱수에 대해서 배수를 구한다. 8/(2*2) = 2
# 다음으로 세제곱수에 대해서 배수를 구한다. 8/(2*2*2) = 1
# 즉 4 + 2 + 1이란 것이다.
n, m = map(int, input().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))