import random

number = random.randint(1, 5)

r = 0
i = 0
while r != number:
    i += 1
    r = input("Guess a number between 1 and 5: ") 
    if r.isnumeric():
        r = int(r)
else:
    print(f'You guessed it in {i} tries!')