import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
print(arr2)
dic = {arr2[i] : i for i in range(len(arr2))} # key = numbers in arr
                                    # value = key의 값보다 작은 key값의 개수
for i in arr:
    print(dic[i], end = ' ')