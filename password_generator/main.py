import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "~`!@#$%^&*()_+-={}[]:;'<>,.?/|\\"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

#Length of the password
length = 20

#amount of passwords to generate
amount = 10

for x in range (amount):
    #Using sample method to pick random values from the all string without replacement
    password = "".join(random.sample(all, length))
    print(password)
