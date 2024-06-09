import random
def heads_or_tails():
    while True:
        toss=input("""Here's the Toss.
        Choose H for Heads or T for Tails""")
        toss=toss.upper()
        tossd=['H','T']
        if toss in tossd:
            break
        else:
            print("Wrong Input")
            toss=toss.upper()

    ctoss=random.choice(tossd)
    dl=['bat','ball']
    if ctoss==toss:
        d=input("You won the toss.Would you like to bat or ball?")
        d=d.lower()
        while True:
            if d not in dl:
                d=input("Enter a valid input")
            else:
                break
        if d=="bat":
            compball()
        else:
            compbat()
        
    else:
        cd=random.choice(dl)
        print(f"You lost the toss.The computer chose to {cd}")
        if cd=="bat":
            compbat()
        else:
            compball()
  

def compbat():
    ctotal=0
    poss=['1','2','3','4','5','6']
    while True:
        uc=int(input("Choose a number from 1 to 6"))
        while True:
            if uc>6:
                uc=int(input("Choose a number from 1 to 6"))
            else:
                break
        cc=random.choice(poss)
        if uc==int(cc):
            print(f"The computer chose {uc}")
            print(f"The computer is out with a score of {ctotal}")
            break
        else:
            print(f"The computer chose {cc}")
            ctotal=ctotal+int(cc)
            print(f"The computer's total is {ctotal}")
            print()
    print()

    print("You're batting now")
    utotal=0
    poss=['1','2','3','4','5','6']
    while True:
        uc=int(input("Choose a number from 1 to 6"))
        while True:
            if uc>6:
                uc=int(input("Choose a number from 1 to 6"))
            else:
                break
        cc=random.choice(poss)
        if uc==int(cc):
            print(f"The computer chose {uc}")
            print(f"You're out with a score of {utotal}")
            break
        else:
            print(f"The computer chose {cc}")
            utotal=utotal+uc
            print(f"Your total is {utotal}")
            print()
            if utotal>ctotal:
                break
    if ctotal>utotal:
        print("The computer won the game. Better luck next time!!")
    elif ctotal==utotal:
        print("It's a draw")
    else:
        print("Congratulations you won the game!!")
            
def compball():
    utotal=0
    poss=['1','2','3','4','5','6']
    while True:
        uc=int(input("Choose a number from 1 to 6"))
        while True:
            if uc>6:
                uc=int(input("Choose a number from 1 to 6"))
            else:
                break
        cc=random.choice(poss)
        if uc==int(cc):
            print(f"The computer chose {uc}")
            print(f"You're out with a score of {utotal}")
            break
        else:
            print(f"The computer chose {cc}")
            utotal=utotal+uc
            print(f"The total is {utotal}")
            print()
    print()
    
    print("Its's the computer's turn to bat")
    ctotal=0
    poss=['1','2','3','4','5','6']
    while True:
        uc=int(input("Choose a number from 1 to 6"))
        while True:
            if uc>6:
                uc=int(input("Choose a number from 1 to 6"))
            else:
                break
        cc=random.choice(poss)
        if uc==int(cc):
            print(f"The computer chose {uc}")
            print(f"The computer is out with a score of {ctotal}")
            break
        else:
            print(f"The computer chose {cc}")
            ctotal=ctotal+int(cc)
            print(f"The computer's total is {ctotal}")
            print()
            if ctotal>utotal:
                break
    if ctotal>utotal:
        print("The computer won the game. Better luck next time!!")
    elif ctotal==utotal:
        print("It's a draw")
    else:
        print("Congratulations you won the game!!")

print(''.center(80, '*'))        
print("\t\t\tYou're Playing Hand Cricket")
print("RULES")
print("You can select only a number from 1 to 6")
print("Let's start the game")
print()
while True:
    heads_or_tails()
    dd=input("Choose Y to play again or N to exit")
    dd=dd.upper()
    y=['Y','N']
    while True:
        if dd not in y:
            dd=input("Choose Y to play again or N to exit")
            dd=dd.upper()
        else:
            break
    if dd=='N':
        break
    else:
        print("Restarting the game. Hang on!!")
        print()
        print(''.center(80, '*'))
    
    


    
    




    
