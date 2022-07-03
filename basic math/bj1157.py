from collections import Counter
word = input()
word = word.lower()
char_set = (Counter(word).most_common(2))
if len(word)==1:
    print(word.upper())
elif (char_set[0][1]) == (char_set[1][1]):
    print("?")
elif (char_set[0][1]) > (char_set[1][1]):
    print(char_set[0][0].upper())
else:
    print(char_set[1][0].upper())