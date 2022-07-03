alpha_list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word = input()
time = 0
for i in alpha_list: #alpha_list의 요소 추출
    for j in i:      #위에서 뽑은 요소를 하나의 문자로 나눔
        for x in word:
            if j == x:
                time += 3 + alpha_list.index(i)
                
print(time)