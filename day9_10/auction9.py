from logoday9 import logo
print(logo)
print("welcome to auction bid")
dict={}
name=input("enter your name \n")
bid=int(input("enter your bid \n"))
dict[name] = bid
next_user=input("are there any other bidders? type 'yes' or 'no'\n")
while next_user=='yes':
   print("\n"*100)
   name=input("enter your name \n")
   bid=int(input("enter your bid \n"))
   dict[name] = bid
   next_user=input("are there any other bidders? type 'yes' or 'no'\n")

highest_bid=0
winner=''
for name in dict:
   if highest_bid<dict[name]:
      highest_bid =dict[name]
      winner=name
print(dict)
print(f"highest bid is {highest_bid}")
print(f"winner is {winner}" )


