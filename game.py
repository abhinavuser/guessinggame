import random 
num = random.randint(1,100)
print("Welcome to The Guessing Game")
print("I am currently thinking of a number between 1 and 100")
print("You are COLD if you are more than 10 away from the number I am thinking of")
print("You are WARM if you are within 10 from the number I am thinking of")
print("You are COLDER, If you guess farther away from your most recent guess ")
print("You are WARMER, If you guess closer to your most recent guess")
print("Let's Start")
guess = [0]
while True:
    user_input = int(input("I am thinking of a number between 1 and 100, Enter your guess: "))

    if user_input > 100 or user_input < 1:
        print("Out of Bounds, Try again")
        continue

    if user_input == num:
        print(f"Congratulations, You have guessed correctly in only {len(guess)} guesses")
        break

    guess.append(user_input)

    if guess[-2]:
        if abs(num - user_input) < abs(num - guess[-2]):
            print('Warmer')
        else:
            print("Colder")

    else:
        if abs(num - user_input) <=10 :
            print("Warm")
        elif abs(num - user_input) > 10:
            print('Cold')

#guessing game
