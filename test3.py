positives = [int(digit) for digit in input().split(", ") if int(digit) >= 0]
negatives = [int(digit) for digit in input().split(", ") if int(digit) < 0]
evens = [int(digit) for digit in input().split(", ") if int(digit) % 2 == 0]
odds = [int(digit) for digit in input().split(", ") if int(digit) % 2 != 0]
print(f"Positive: {positives}\n"
      f"Negative: {negatives}\n"
      f"Even: {evens}\n"
      f"Odd: {odds}")