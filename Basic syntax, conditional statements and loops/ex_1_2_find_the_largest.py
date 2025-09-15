word = input()
capital_letters = []
for index in range(len(word)):
   if word[index].isupper():
       capital_letters.append(index)

print(capital_letters)


#вириант 2

#word = input()
#new_string = '['

#for index in range(len(word)):
#    if word[index].isupper():
#        new_string += str(index) + ", "

#if len(new_string) > 1:
#    new_string = new_string[: -2]

#new_string += "]"
#print(new_string)


