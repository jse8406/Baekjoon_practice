n = int(input())
people = []
for i in range(n):
   age, name = map(str, input().split())
   age = int(age)
   people.append((age, name))
people.sort(key = lambda x: x[0]) # key값 lambda 비교 우선순위 설정 가능
                                  # -를 붙이면 역순으로, 우선순위 여러개 설정 가능
                                  # 우선순위 기입 순서대로 가중치가 
for i in people:
    print(i[0], i[1])