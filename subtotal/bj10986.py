N, M = map(int, input().split())
a = list(map(int, input().split())) + [0]
cnt = [0] * M

for i in range(N):
    a[i] += a[i - 1] # 누적합 구하기
    cnt[a[i] % M] += 1 # 누적합을 3으로 나눈 나머지에 해당하는 인덱스의 값 1증가

ans = cnt[0] # 누적합의 3 모듈러가 0인 수는 그자체로 나머지가 되므로 0의
             # 인덱스의 값이 구간의 개수로 바로 포함

for v in cnt:
    ans += v * (v - 1) // 2 #나머지가 같은 것끼리 vC2 조합을 이용

print(ans)

