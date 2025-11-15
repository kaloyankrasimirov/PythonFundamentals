import re
full_name = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
match = re.findall(pattern, full_name)
print(' '.join(match))