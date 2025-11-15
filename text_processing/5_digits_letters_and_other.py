string = input()
numbers = ''
letters = ''
chars = ''

for char in string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        chars += char

print(f"{numbers}\n"
      f"{letters}\n"
      f"{chars}")