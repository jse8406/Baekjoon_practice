arr1 = []
arr2 = []
n1, m1 = map(int, input().split())
for _ in range(n1):
  l1 = list(map(int, input().split()))
  arr1.append(l1)
n2, m2 = map(int, input().split())

for _ in range(n2):
  l2 = list(map(int, input().split()))
  arr2.append(l2)
  
answer = [[0 for _ in range(m2)] for _ in range(n1)]
for n in range(n1):
    for k in range(m2):
        for m in range(m1):
            answer[n][k] += arr1[n][m] * arr2[m][k]

for i in answer:
  print(*i)
  
  
  # N*M 행렬 x M*K 행렬 = N*K행렬이 된다.