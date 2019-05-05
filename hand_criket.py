import random

#toss--------------------------------------------------------------------------

toss1=['Heads','Tails']
#toss1=['Heads' for i in range(100) if i%2==0]
choice=['Bat','Ball']

toss=random.choice(toss1)
choice1=random.choice(choice)

choose2=int(input("Choose head or tails\n1.Heads\n2.Tails\n\n"))
if choose2==1:
    choose1="Heads"
else:
    choose1="Tails"

#batting or balling selection  -------------------------------------------------------

if (choose1==toss):
    choose=int(input("\nWhat you want to choose\n1.Bat\n2.Ball\n\n"))
    if (choose==1):
        choose3="Bat"  #player_variable
        bat=0
        ball=1
    else:
        choose3="Ball" #player_variable
        ball=0
        bat=1
else:
    print("\nComputer wins and choose to" ,choice1, "\n")  #computer_variable
    if choice1=="Bat":
        bat=1
        ball=0
    else:
        ball=1
        bat=0

if bat==0 or ball==1:
    print("Your turn to bat\n")
    final_chance="user"
else:
    print("Computer turn to bat\n")
    final_chance="comp"

##############################################################################################
#----------------------------------------Main Game-------------------------------------------#
##############################################################################################

player_choice=0
computer_choice=-1
player_points=0
computer_points=0

if final_chance=="user":        #User batting first
    while player_choice!=computer_choice:
        player_points+=player_choice
        player_choice=int(input("you choose !!\n"))
        computer_choice=random.randint(0,6)
        print("Computer choose"  ,computer_choice)
        print("\n")

    print("You are out\n\n                 Your score is" ,player_points)
    print("\n")                               #user out now computer bat
    
    print("\nNow Computer turns to bat\n")
    
    player_choice=0
    computer_choice=-1

    while player_choice!=computer_choice:
        computer_points+=computer_choice
        player_choice=int(input("you choose !!\n"))
        computer_choice=random.randint(0,6)
        print("computer choose"  ,computer_choice )
        print("\n")

    print("Computer Out\n\n                  Computer score is" ,computer_points)
    print("\n")#---------------------------
else:          
    while player_choice!=computer_choice:       #computer bat  first
        computer_points+=computer_choice
        player_choice=int(input("you choose !!\n"))
        computer_choice=random.randint(0,6)
        print("Computer choose"  ,computer_choice)
        print("\n")

    print("\nComputer Out\n                  Computer score is" ,computer_points)
    print("\n")                               #computer out now user bat
    
    print("\nNow Your turns to bat\n")
    
    player_choice=0
    computer_choice=-1

    while player_choice!=computer_choice:
        player_points+=player_choice
        player_choice=int(input("you choose !!\n"))
        computer_choice=random.randint(0,6)
        print("computer choose"  ,computer_choice )
        print("\n")

    print("\nPlayer Out\n                    Player score is" ,player_points)
    print("\n")
    
  
if player_points>computer_points:
    print("User Wins")
else:
    print("Computer Wins")