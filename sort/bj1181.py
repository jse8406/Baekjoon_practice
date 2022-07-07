def mergeSort(list):
    size = len(list)
    if size <= 1:
        return list
    mid = len(list)//2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    merged_list = merge(left, right)
    return merged_list

def merge(list1, list2):
    merged = []
    while len(list1) > 0 and len(list2) > 0:
        if len(list1[0]) < len(list2[0]):
            merged.append(list1.pop(0))
        elif len(list1[0]) == len(list2[0]):
            i = 0
            while list1[0][i] == list2[0][i]:
                i += 1           
            if list1[0][i] < list2[0][i]:
                merged.append(list1.pop(0))
            else:
                merged.append(list2.pop(0))
        else:
            merged.append(list2.pop(0))
    if len(list1)>0:
        merged += list1
    else:
        merged += list2
    return merged

n = int(input())
words = []
for i in range(n):
    words.append(input())
words = list(sorted(set(words)))
words = mergeSort(words)
for i in words:
    print(i)