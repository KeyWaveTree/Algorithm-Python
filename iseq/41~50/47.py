word = input()
w = input()
arrow = int(input())

if w=='L' or w=='l':
    word=word[arrow:]+word[:arrow]

if w=='R' or w=='r':
    word=word[len(word)-arrow:]+word[:len(word)-arrow]

print(word)

