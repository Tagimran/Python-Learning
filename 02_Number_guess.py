import random 

number = random.randint(1,10)
attempts = 0

while True :
    guess = int(input("Guess a Number (1-10): "))
    attempts += 1
    if guess == number:
        print(f"Correct You guessed it in {attempts} attempts.")
        break
    elif guess<number:
        print("Too Low, try again")
    else:
        print("Too High, try again")
        