def recursion(s, l, r):
    recursion.counter += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

recursion.counter = 0
num = int(input())
words = list()
for i in range(num):
    word = input()
    words.append(word)
for i in range(num):
    print(isPalindrome(words[i]), recursion.counter)
    recursion.counter = 0