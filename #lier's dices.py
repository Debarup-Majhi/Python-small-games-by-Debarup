#lier's dices
""" phaes 
1. rolling 
2. bidding  """
#cups and dices
#each has 5 dices
#there are 3 options 
'''1. raise the bid
2. call Buff
3. call spot on '''
#losing the bid then 1 dice will reduce in next round
#win spot on then other has to reduce 1 dice each and if lose the remove 2 dice

#each round will be called by a function
#each dice will be a list

import random
def selection(diceleft): #give a list containg element of dice
    l=[]
    for i in range(diceleft):
        a = random.randint(1,6)
        l.append(a)
    return l

#def rolling(noofplayer,no_of_diceleft_list): #gives a list of list
    k=[]
    for i in range(noofplayer):
        s = selection(no_of_diceleft_list[i])
        k.append(s)
    return k

def rolling2(d):
    k={}
    for i,j in d.items() :
        s= selection(j)
        k[i] = s
    return k

def nameing(noofplayer):
    namelist=[]
    for i in range(1,noofplayer+1):
        name=input(f"enter name of {i}st player: ")
        namelist.append(name)
    return namelist 

def no_of_diceleft(namelist):
    l={}
    for i in namelist:
        no = int(input(f"enter the number of dice player {i} has:"))
        l[i] = no
    return l



n = int(input("enter number of players:"))
namelist=nameing(n) #store a list of names of player
score_card_dic= no_of_diceleft(namelist) #store (name_of_player:dice_left)
dicelist=rolling2(score_card_dic) #store (name_of_player:dices_he/she_have)








    

    