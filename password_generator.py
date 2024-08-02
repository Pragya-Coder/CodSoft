import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '()[]{},:;.-/?+#*\\'

upper, lower, nums, syms = True, True, True, True

chars = ""

if upper:
    chars += uppercase_letters
if lower:
    chars += lowercase_letters
if nums:
    chars += digits
if syms:
    chars += symbols

length = 25
amount = 12

for x in range(amount):
    password = "".join(random.sample(chars, length))

print(password)