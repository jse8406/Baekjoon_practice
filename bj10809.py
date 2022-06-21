alpastr = [] # 알파벳 저장
str = list(input())
storage = [] # 알파벳 수 만큼 -1 저장
for i in range(26):
    storage.append(-1)
    alpastr.append(chr(i+97))
for i in str:
    if storage[alpastr.index(i)] == -1:
        storage[alpastr.index(i)] = str.index(i)
for i in range(26):
    print(storage[i], end=" ")
    
#모범 답안 훨씬더 짧다   
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)), end=" ") # find함수 찾는 문자가 존재 한다면 해당 위치의 index를
                                      #반환해주고찾는 문자가 존재 하지 않는다면 -1 을 반환합니다.