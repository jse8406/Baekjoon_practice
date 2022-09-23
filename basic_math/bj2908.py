num = input().split()
first = []
sec = []
for i in num[0]:
    first.append(i)                 #쓸데없는 코드가 너무 많다
first.reverse()                     #쓸데없는 코드가 너무 많다
first =''.join(map(str, first))     #쓸데없는 코드가 너무 많다
for i in num[1]:                    #쓸데없는 코드가 너무 많다
    sec.append(i)                   #쓸데없는 코드가 너무 많다  
sec.reverse()                       #쓸데없는 코드가 너무 많다
sec =''.join(map(str, sec))         #쓸데없는 코드가 너무 많다
if first > sec:                     #쓸데없는 코드가 너무 많다
    print(first)                    #쓸데없는 코드가 너무 많다
else:
    print(sec)