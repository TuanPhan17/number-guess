import random 
print(" Guess the number (1-100)")

secret = random.randint(1, 100)

tries = 0
while True:
    guess_raw = input("Your guess: ").strip()

    if not guess_raw.isdigit():
        print("Enter a whole number 1-100.")
        continue

    guess = int(guess_raw)
    if guess < 1 or guess > 100:
        print("Stay within 1-100.")
        continue

    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too High")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break