key = int(input())
number_of_lines = int(input())

decrypted_message = []

for _ in range(number_of_lines):
    input_char = input()
    new_char = chr(ord(input_char) + key)
    decrypted_message.append(new_char)

print("".join(decrypted_message))

