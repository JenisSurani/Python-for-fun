import random

print("Welcome To the Snake Water Gun program\n\n")

Options=["Snake","Water","Gun"]

# comp:  S W G
# user:S:T W L
    #  W:L T W
    #  G:W L T 

# 1 means Win
# 0 means Lose
# -1 means Tie

Rules=[
       [-1,1,0],
       [0,-1,1],
       [1,0,-1]
      ]

comp_score=0
user_score=0

for i in range(10):
    print(f"\nROUND {i+1}:")
    while True:
        try:
            User_input=int(input("Your Turn: 0 for Snake , 1 for Water and 2 for Gun: "))
            print(f"You Choose {Options[User_input]}")
            break
        except:
            print("Please Enter valid number")

    Computer_input=random.randint(0,2)
    print(f"Computer Choose {Options[Computer_input]}")

    answer=Rules[User_input][Computer_input]
    print(f"\nRound-{i+1} Result:")
    if answer==1:
        print("User wins!!")
        user_score+=1
    elif answer==0:
        print("Computer wins!!")
        comp_score+=1
    else:
        print("Tie!!")
    print(f"COMPUTER SCORE: {comp_score}",f"USER SCORE: {user_score}")

if(comp_score>user_score):
    print("\nCOMPUTER WINS THE GAME")
elif(user_score>comp_score):
    print("\nUSER WINS THE GAME")
else:
    print("\nGAME ENDS IN TIE")

# Author: Jenis Surani
# Topic: SnakeWaterGun
# Date: 14/02/2025