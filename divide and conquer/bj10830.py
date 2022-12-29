arr1 = []

N, B = map(int, input().split())
for _ in range(N):
  l1 = list(map(int, input().split()))
  arr1.append(l1)

def mul(a ,b):
  n = len(a)
  result = [[0]*n for _ in range(n)]
  for row in range(n):
    for col in range(n):
      val = 0
      for i in range(n):
        val += a[row][i] * b[i][col]
      result[row][col] = val % 1000
  return result

def square(A, B):
  if B == 1:
    for x in range(len(A)):
      for y in range(len(A)):
          A[x][y] %= 1000
    return A
  tmp = square(A, B//2)
  if B % 2:
    return mul(mul(tmp,tmp), A)
  else:
    return mul(tmp, tmp)

result = square(arr1, B)
for r in result:
  print(*r)
  
# 지수를 2 로 나누어 계산 횟 수를 줄인다 = divide and conquer, 재귀는 거의 모든 문제의 기초가 된다,  