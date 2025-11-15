word = input()

new_word = [symbol for symbol in word if symbol.lower() not in ["a", "e", "o", "u", "i"]]
print("".join(new_word))
