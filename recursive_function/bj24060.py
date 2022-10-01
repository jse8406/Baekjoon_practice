def merge_sort(A, left, right):
  if left < right:
    middle = (left + right) // 2
    merge_sort(A, left, middle)
    merge_sort(A, middle + 1, right)
    merge(A, left, middle, right)

def merge(A, left, middle, right):
  global count, result
  i, j = left, middle + 1
  tmp = []
  
  while i <= middle and j <= right:
    if A[i] <= A[j]:
      tmp.append(A[i])
      i+= 1
    else:
      tmp.append(A[j])
      j +=1
      
  while i <= middle:
    tmp.append(A[i])
    i += 1
  
  while j <= right:
    tmp.append(A[j])
    j += 1
  i, t = left, 0
    
  while i <= right:
    A[i] = tmp[t]
    count += 1
    if count == k:
      result = A[i]
      break
    i += 1
    t += 1
    
N, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1  
merge_sort(A, 0, N-1)
print(result)
