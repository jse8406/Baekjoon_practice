num = int(input())
for i in range(num):
    ox_list = list(input())
    score = 0
    score_sum = 0
    for j in ox_list:
        if j =="O":
            score +=1
            score_sum += score
        else:
            score = 0
    print(score_sum)