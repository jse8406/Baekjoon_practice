n = int(input())
chats = []
for i in range(n):
    chat = input()
    chats.append(chat)
    
ans = 0

names = set()

for chat in chats:
    if chat != 'ENTER':
        names.add(chat)
    elif chat == 'ENTER':
        ans += len(names)
        names = set()
ans+= len(names)
        
print(ans)