word = input()
print(word[::-1])

#option 2

word = input()
for i in range(len(word) -1, -1, -1):
    print(word[i], end='')