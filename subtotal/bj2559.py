N, K = map(int, input().split())
nums = list(map(int, input().split()))

k_nums = []
for i in range(1, N):
  nums[i] = nums[i] + nums[i-1]
nums = [0] + nums

for i in range(K, N+1):
  k_nums.append(nums[i] - nums[i-K])
print(max(k_nums))