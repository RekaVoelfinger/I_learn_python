import random, string

digits = []
for _ in range(9):
            digits.append(random.choice(string.digits))
print(digits)
