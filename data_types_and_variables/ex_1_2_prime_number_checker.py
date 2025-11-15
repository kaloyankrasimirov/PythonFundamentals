number = int(input())

is_prime = True
if number <= 1:
    is_prime = False

for _ in range(2, number):
    if number % _ == 0:
        is_prime = False
        break

print(is_prime)