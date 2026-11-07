#Black Jack
import random

print("WELCOM TO BLACK JACK")
print("RULES OF GAME:")
print("1. YOU HAVE TO PICK 2 CARDS THEN AFTERWARD 1 CARD IF YOU WANT")
print("2. YOUR CARDS VALUE SHOULD BE LESS THAN 21 ")
print("3. TO WIN YOU MUST GET THE HIGHEST VALUE IN THE WHOLE GAME")
print("   ")

def cards(n=2):
    cards = ["1","2","3","4","5","6","7","8","9","10","ace","jack","king","queen"]
    x=random.choices(cards,weights = [4,4,4,4,4,4,4,4,4,4,4,4,4,4], k = n)
    return x

def nameing(noofplayer):
        namelist=[]
        for i in range(1,noofplayer+1):
            name=input(f"enter name of {i}st player: ")
            namelist.append(name)
        return namelist

class Players:
    def __init__(self,name,cards=list):
        self.name=name
        self.cards=cards

    def show_number(self):
        print("   ")
        print(self.name,"your cards are",self.cards)
        num = 0
        for i in self.cards:
            if i in ["1","2","3","4","5","6","7","8","9","10"]:
                num = num + int(i)
            elif i in ["jack","king","queen"]:
                num = num + 10
            else:
                num = num + 11
                print("Selection of ace will be done later for now it will be taken as 11")
        return num
    
    def Ace(self,num=int):
        print("As you have an Ace among your cards")
        print("Ace has two values: 1 and 11")
        print("accoding to your calculation choss it")
        a = input("Do you want 11 or 1: ")
        if a == "11":
            num = num
        elif a == "1":
            num = num - 10
        return num

    def get_cards(self,a=str):
        print("Giving you a card")
        li=cards(1)
        self.cards.extend(li)
        r = self.show_number()
        print(self.name,"your cards value is:",r)
        

no_of_Player = int(input("Enter how many are playing:"))

name_list = nameing(no_of_Player)

dic_data = {}

for i in name_list:
    i = Players(i,cards())
    num = i.show_number()
    print("The value of all your cards is:",num)

    a = input("Do you want to take another card:(YES/NO)")
    while a.upper() == "YES":
        i.get_cards(a)
        a = input("Do you want to take another card:(YES/NO)")
    else:
        if "ace" in i.cards:
            num = i.show_number()
            k= i.Ace(num)
            print("your cards value is:",k)
            dic_data[i.name] = k
        else:
            r = i.show_number()
            print("your cards value is:",r)
            dic_data[i.name] = r

    
print("the value of all the player are:")
for name,value in dic_data.items():
    print(name,":",value)

winner_data = dic_data.copy()

# wining rules
for name,value in dic_data.items():
    if value > 21:
        print(name,"lost the game as your cards values are more than 21")
        print(" ")
        winner_data.pop(name)

z = "False"
winner = 0
for name,value in winner_data.items():
    
    if value == winner:
        z = "True"
        print("There are two winner so game is draw between",name,winner_name)
    
    elif value > winner:
        winner = value
        winner_name = name
if z == "False":
    print(winner_name,"has win the game as player has higest value:",winner)
    
    


    
 









