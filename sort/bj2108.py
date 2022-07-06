from collections import Counter

def modefinder(list):
    count_list = []
    value_list = []
    c = Counter(list)
    mode = c.most_common()
    leng = len(mode)
    
    for i in range(leng):
        value_list.append(mode[i][0])
        count_list.append(mode[i][1])
    if count_list.count(max(count_list)) == 1:
        return value_list[count_list.index(max(count_list))]
    else:
        ans = []
        most_common_count = count_list.count(max(count_list))
        for i in range(leng):
            if max(count_list) == count_list[i]:
                ans.append(value_list[i])
        ans.remove(min(ans))
        return(min(ans))

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
sorted_li = sorted(li)


print(round(sum(li)/n)) # 산술평균 
print(sorted_li[n//2]) # 중앙값
print(modefinder(li))  # 최빈값
print(max(li) - min(li)) # 범위