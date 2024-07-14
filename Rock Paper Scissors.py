import random
computer=0
player=0

def start(computer,player):
    player=0
    computer=0
    print("""Welcome to Rock Paper Scissors
This is just a simple game of Rock Paper Scissors
The game ends when either the player or the computer get 5 points
Enjoy!!!""")
    main(computer,player)
    
def main(computer,player):
    list1=["Rock", "Paper", "Scissors"]
    cside=random.choice(list1)
    pside=str(input("What do you choose -->"))
    if (pside == "Rock" or pside == "Paper" or pside == "Scissors"):
        check(pside,cside,computer,player)
    else:
        print("Error, Please chooses either 'Rock', 'Paper' or 'Scissors'")
        main(computer,player)

def check(cside,pside,computer,player):
    r="Rock"
    p="Paper"
    s="Scissors"
    if(pside==r and cside==r):
        print("Rock - Rock")
        result="Draw"
    if(pside==p and cside==p):
        print("Paper - Paper")
        result="Draw"
    if(pside==s and cside==s):
        print("Scissors - Scissors")
        result="Draw"
    elif(pside==r and cside==p):
        print("Rock - Paper")
        result="Win"
    elif(pside==p and cside==r):
        print("Paper - Rock")
        result="Loss"
    elif(pside==s and cside==p):
        print("Scissors - Paper")
        result="Win"
    elif(pside==p and cside==s):
        print("Paper - Scissors")
        result="Loss"
    elif(pside==r and cside==s):
        print("Rock - Scissors")
        result="Win"
    elif(pside==s and cside==r):
        print("Scissors - Rock")
        result="Loss"
    Result(result,computer,player)

def Result(result,computer,player):
    if(result=="Draw"):
        print("The Match Is A Draw")
    elif(result=="Win"):
        print("You won")
    elif(result=="Loss"):
        print("You Lost")
    score(result,computer,player)

def score(result,computer,player):
    next="No"
    if (result=="Loss"):
        computer=computer+1
    elif(result=="Win"):
        player=player+1
    else:
        pass
    print("The Score is: Player-->", player ,"Computer-->", computer)
    if (player==5):
        print("You Have Won The Game")
    elif(computer==5):
        print("You Have Lost The Game")
    else:
        main(computer,player)
    Next(computer,player)

def Next(computer,player):
    next=str(input("Do you want to play again?-->"))
    if(next=="Yes"):
        start(computer,player)
    elif(next=="No"):
        exit()
    else:
        print("Error, Please choose either 'Yes' or 'No'")
        Next(computer,player)
start(computer,player)