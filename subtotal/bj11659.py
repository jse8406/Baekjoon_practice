# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# for i in range(M):
#   start, end = map(int, input().split())
#   print(sum(nums[start-1:end]))
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1,N):
  nums[i] += nums[i-1]
nums = [0] + nums

for _ in range(M):
  start, end = map(int, input().split())
  print(nums[end]- nums[start-1])
  
  # 구간합을 구할 때마다 구간을 탐색하며 합을 구하면
  # i ~ j 까지의 구간합을 구하면 O(j-i+1) 이고 이러한 질의가 n개이면
  # O((j-i+1)xn) 이 된다. 
  
  # 하지만 리스트에서 특정 인덱스의 값을 탐색하는 것은 O(1)이기 때문에 
  # 누적합을 미리 구해놓고 구간합을 구하기 위해 누적합끼리의 차를 구하면
  # 시간 복잡도가 누적합을 구하는 O(N)이외에는 없다. 따라서 시간을 훨씬 절약할 수 있다.