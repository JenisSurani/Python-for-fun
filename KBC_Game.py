import sys

print("Welcome To KBC, Me Amitabh Bachchan apka swagat karta hoon..")
print("On The Hot-seat:", input("Please Enter your name: "))

list_of_questions = [
    ["What is the capital of India?", "A) Mumbai", "B) Kolkata", "C) New Delhi", "D) Chennai", "C"],
    ['Who is known as the "Missile Man of India"?', "A) Homi Bhabha", "B) Vikram Sarabhai", "C) Abdul Kalam", "D) C.V. Raman", "C"],
    ["Which planet is known as the Red Planet?", "A) Venus", "B) Mars", "C) Jupiter", "D) Saturn", "B"],
    ["Which is the largest ocean on Earth?", "A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean", "D"],
    ["What is the national currency of Japan?", "A) Yen", "B) Rupee", "C) Won", "D) Ringgit", "A"],
    ['Which Indian cricketer is known as "God of Cricket"?', "A) Virat Kohli", "B) MS Dhoni", "C) Sachin Tendulkar", "D) Kapil Dev", "C"],
    ["Which is the longest river in the world?", "A) Amazon", "B) Ganga", "C) Nile", "D) Yangtze", "C"],
    ["What is the chemical symbol for Gold?", "A) Ag", "B) Au", "C) Pb", "D) Fe", "B"],
    ["Which Mughal emperor built the Taj Mahal?", "A) Akbar", "B) Shah Jahan", "C) Aurangzeb", "D) Jahangir", "B"],
    ['Who wrote the Indian national anthem "Jana Gana Mana"?', "A) Rabindranath Tagore", "B) Bankim Chandra Chattopadhyay", "C) Mahatma Gandhi", "D) Subhash Chandra Bose", "A"],
    ["What is the square root of 144?", "A) 10", "B) 12", "C) 14", "D) 16", "B"],
    ["Which of the following is NOT a programming language?", "A) Python", "B) HTML", "C) Java", "D) C++", "B"],
    ["What is the full form of RAM in computers?", "A) Randomly Accessed Memory", "B) Read Access Memory", "C) Random Access Memory", "D) Run Access Memory", "C"],
    ["Which is the national bird of India?", "A) Peacock", "B) Eagle", "C) Parrot", "D) Pigeon", "A"],
    ["Which planet is closest to the Sun?", "A) Venus", "B) Mercury", "C) Earth", "D) Mars", "B"],
    ["Who discovered gravity?", "A) Albert Einstein", "B) Isaac Newton", "C) Galileo Galilei", "D) Nikola Tesla", "B"]
]

list_pricePool = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
money = 0
isExited=False
currentPriceWon = 0

for i in range(len(list_of_questions)):
    
    print(i)       
    if isExited==True:
        i=i-1
        print("you answer",i,"correct answer")
        
        if i<4:
             currentPriceWon=0
             break
            
        if i >= 4:
            currentPriceWon = 10000
            break
            
        elif i >= 9:
            currentPriceWon = 320000
            break
            
        elif i >= 14:
            currentPriceWon = 7500000
            break
            
        elif i >= 16:
            currentPriceWon = 75000000
            break

        
        
    while True:
        
        Que = list_of_questions[i]
        print("\n", "-" * 50)
        print("Question", i + 1, ":", Que[0])
        print(Que[1], Que[2], "\n", Que[3], Que[4])

        print("Enter your answer: (A/B/C/D) and 0 to exit")
        ans = input().strip().upper()
        if ans.startswith("0"):
            # user want to quit
            if(i!=0):
               currentPriceWon = list_pricePool[i-1]
            else:
                currentPriceWon=0
            print("You won", currentPriceWon)
            exit()
        else:
            print("Lock kiya jaiye? (Yes/No)")
            Loc = input().strip().lower()

            if Loc.startswith("yes"):
              islocked = True
              break
            else:
              print("Asking Question Again!!")
              continue  # Goes back to the same question
        

       
    if ans == Que[5]:
            print("Correct answer! You won", list_pricePool[i])
    else:
            print("Wrong answer! The correct answer was:", Que[5])
            print("Game Over!")
            isExited=True

       

print("\n", "-" * 100)
print("Game Over! The money you bring home is:", currentPriceWon)


# Author: Jenis Surani
# Topic: KBC-Game
# Date: 07/02/2025
