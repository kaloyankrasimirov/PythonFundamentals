import re
sentence = input()
searched_word = input()
# pattern = fr'\b{searched_word}\b'
# matches = re.findall(pattern, sentence, re.IGNORECASE)
pattern = fr'(?i)\b{searched_word}\b'
matches = re.findall(pattern, sentence)
print(len(matches))
