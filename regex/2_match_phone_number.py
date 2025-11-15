import re
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
numbers = input()
match = re.findall(pattern, numbers)
print(", ".join(match))