num = int(input())
group_word = 0
#error = 0 처음 error 변수 위치
for i in range(num):
    word = input() #bb
    error = 0
    for i in range(len(word)-1): #1
        if word[i] != word[i+1]:
            if word[i+1:].count(word[i])>0:
                error += 1
    if error == 0:
        group_word += 1
print(group_word)