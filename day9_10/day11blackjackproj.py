import random
choice=input("do yoou want to play blackjack game? Type 'y' for yes, 'n' for no" )
l1=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def calc_sum(cards):

    total=sum(cards)
    if 11 in cards and total>21:
        cards.remove(11)
        cards.append(1)
        total=sum(cards)

    print(f"your cards {cards},total={total}")
    return total

def card():
    if choice=='y':
        usercards=random.choices(l1,k=2)
        compcards=random.choices(l1,k=2)

        ucards=calc_sum(usercards)
        ccards=calc_sum(compcards)

        print(f"computer's first card: {compcards[0]}")
        goforward=input("type 'y' to go forwadrd and type 'n' to pass: ")
        while goforward:
            if goforward=='y':
                usercards.append(random.choice(l1))
                print(usercards)
                calc_sum(usercards)
                goforward = input("type 'y' to go forwadrd and type 'n' to pass: ")
            else:
                break





card()
