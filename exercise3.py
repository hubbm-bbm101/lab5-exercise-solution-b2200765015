from random import choice
guess1=int(input("Make a guess(Between 100 and 1):"))
number=choice(range(100))
print(number)
while True:
    if guess1 == number:
        break
    elif guess1 < number:
        print("increase your number")
    else:
        print("decrease your number")
    guess1=int(input(""))
print("You won. It is:",number)