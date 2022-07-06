n = int(input())
a = [0]*10000
for i in range(n):
    a.append(int(input()))
a.sort()
for i in a:
    print(i)
    
""" bubble sort """
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]  

# 사실 버블 정렬은 제일 큰 값을
# 제일 뒤로 밀어냈으면 그 값은 이제 제외하고 비교해도 되지만 이 여기선
# 그냥 계속 제일 마지막까지 비교한다
# 시간 복잡도 : O(n^2)

""" insert sort """
# for i in range(1, len(M)):
#     while  (i>0) and (a[i] < a[i-1]):
#         a[i], a[i-1] = a[i-1], a[i]
#         i -= 1
# 삽입 정렬은 버블 정렬과 비슷하지만
# 점점 비교 범위를 확장해 비교 시간복잡도 (n^2)/2 = O(n^2)