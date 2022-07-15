count = int(input())
width = []
length = []
total = []
for i in range(6):
    a,b = map(int, input().split())
    total.append(b)
    if a == 1 or a == 2:
        width.append(b)
    else:
        length.append(b)
max_wid = max(width)
max_len = max(length)
max_wid_index = total.index(max_wid)
max_len_index = total.index(max_len)
sub_wid = abs(total[max_len_index - 5] - total[max_len_index - 1])
sub_len = abs(total[max_wid_index - 5] - total[max_wid_index - 1]) 
area = max_len * max_wid - sub_wid * sub_len
print(area * count)