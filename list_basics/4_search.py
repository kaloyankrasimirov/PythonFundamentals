number = int(input())
word = input()

my_list = []
my_new_list = []

for _ in range(number):
    current_word = input()
    my_list.append(current_word)

for item in my_list:
    if word.lower() in item.lower():
        my_new_list.append(item)

print(my_list)
print(my_new_list)


