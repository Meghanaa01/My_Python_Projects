import random
import art
from gamedata import data
print(art.logo)
choice1=random.choice(data)
# print(choice1)
score=0
while True:
    print(f"compare A : {choice1['name']},{choice1['description']} from {choice1['country']}")

    print(art.vs)
    choice2=random.choice(data)

    Afollowers=choice1['follower_count']
    Bfollowers=choice2['follower_count']
    # print(choice2)
    print(f"Against B : {choice2['name']},{choice2['description']} from {choice2['country']}")
    user_guess=input("who has more followers, Type A or B\n").lower()
    # print(user_guess)

    if user_guess=='a':
            if Afollowers>Bfollowers:
                score+=1
                choice1=choice2
                print(f"correct guess,your score is {score}")

            else:
                print(f"wrong guess ,you lose,your final score is {score}")
                break
    elif user_guess=='b':
            if Bfollowers>Afollowers:
                score+=1
                choice1=choice2
                print(f"correct guess,your score is {score}")
            else:
                print(f"wrong guess, you lose,your final score is {score}")
                break


