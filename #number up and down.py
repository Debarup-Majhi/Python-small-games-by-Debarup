#number up and down
import random

# entry = int(input("enter the lowest number to start the game:"))
# exit = int(input("enter the highest number to start the game:"))

print("""welcome, in this game.
In this game you have to guess a number 
this system has generated a number you have to guess a that number 
the number is between 0 to 100 """)

flag = "True"
while flag=="True":
    guess = random.randint(1,100)
    print(" ")
    
    n = int(input("enter your number you guessed: "))
    c = 1
    while n != guess:
        c = c + 1
        if n>guess:
            print("original number is lower")
            n = int(input("guess again: "))
        elif n<guess:
            print("original number is higher")
            n = int(input("guess again: "))
    else:
        print("Your guess is correct, you take " + str(c) + " attempts")
        f = input("Do you want to play another game(Y/N)")
        
        if f.upper() == "Y" :
            flag = "True"
        else:
            flag = "False"
            print("Thankyou for playing")













