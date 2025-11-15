import re
email_input = input()
pattern = r"\s(([a-z0-9]+)([a-z0-9\.\_\-]*)([a-z0-9]+)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, email_input)
for email in matches:
    print(email[0])
