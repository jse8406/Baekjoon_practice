# croatia = ["c=", "c-", "d-", "lj", "nj", "s=", "z=", "dz="]

# word = input()
# sum_len = 0
# for i in croatia:
#     if i == "dz=" and i in word:
#         sum_len += 2
#     elif i in word:         #크로아티아 단어가 반복되면 1번밖에 안센다.
#         sum_len += 1
# print(len(word)-sum_len)
croatia = ['dz=', "c=", "c-", "d-", "lj", "nj", "s=", "z="]
word = input()
for i in croatia:
    word = word.replace(i,'*')
print(len(word))  

# 예제2번의 입력 예시가 ddz=z=인데 만약 croatia의 리스트 요소
# 'dz='의 순서가 더 뒤로 밀려난다면 포문 과정에서 ddz=z=은
# 리스트의 "z="에 의해 먼저 *로 바뀌어 ddz=z=는 dd**로 바뀌어 문자길이가
# 4가 된다. "dz="이 더 앞에 있다면 ddz=z=는 d**로 바뀌어 길이가 3이 된다.
# 약간의 애로사항이 있다