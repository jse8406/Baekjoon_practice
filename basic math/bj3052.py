from collections import Counter

a = [int(input()) for i in range(10)] #엔터로 구분에서 배열입력받기
b = []
for j in range(10):
    b.append(a[j]%42) #배열b에 나머지저장
counter = Counter(b)
dic = dict(counter)
print(len(dic.keys()))