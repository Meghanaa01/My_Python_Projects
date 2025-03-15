import random
print("welcome to number guessing game")
print("i am thinking of a number between 1 and 100")
difficulty=input("choose a difficulty level, easy or hard\n").lower()

chosen_num=random.choice(range(1,101))
if difficulty=='easy':
    n=10
elif difficulty=='hard':
    n=5
else:
    print("enter valid input")
while n>=1:

        print(f"u have {n} attempts to get the number")
        user_guess = int(input("make a guess: "))


        if user_guess<chosen_num:
                print("thats too low, ")
        elif user_guess>chosen_num:
                print("thats too high,")
        elif user_guess == chosen_num:
                print("you guessed it right,You won")
                break
        if n==1 and user_guess!=chosen_num:
                print("you lost, no more attempts left")
        n = n - 1



