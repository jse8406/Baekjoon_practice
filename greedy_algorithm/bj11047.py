n, k = map(int, input().split())
coin_values = []
ans = 0
idx = 0
for i in range(n):
  value = int(input())
  coin_values.append(value)

while True:
  if coin_values[idx] < k and idx < n-1:
    idx += 1      # 배열의 인덱스 처리를 잘 해야한다. idx가 n보다 커지면 인덱스 오류가 난다
  else: 
    break
while k != 0:   
  ans += k // coin_values[idx]
  k -= k//coin_values[idx] * coin_values[idx]
  idx -= 1
print(ans)
