# Rock, paper, sizzers game in Python
from time import sleep
from random import choice
from random import uniform
list=("rock.","paper.","sizzers.")
def manual():
    you=input("Please type R for rock, P for paper, or S for sizzers.")
    if you == "r":
        print ("Rock!")
    elif you == "p":
        print ("Paper!")
    elif you == "s":
        print ("Sizzers!")
    elif you != ("r","s","p"):
        print ("Invalid move. Please try again.")
        manual()
    sleep(uniform(0.7,2.5))
    print ("I choose ",choice(list))
def auto():
    sleep(uniform(2.5,5))
    print ("You choose ",choice(list))
    sleep(uniform(0.7,2.5))
    print ("I choose ",choice(list))
loop = 1
while loop==1:
    mode=input("Welcome to the rock, paper, sizzers game. Please select a mode of gameplay. Press 1 for manual mode, or press 2 for automatic mode (Beta). Press 3 if you want the computer to select the modes for you.")
    if mode == "1":
        print ("You have selected manual mode.")
        loop=0
    elif mode == "2":
        print ("You have selected the automatic mode.")
        loop=0
    elif mode == "3":
        print ("You have selected the random mode")
        loop=0
    else:
        print ("Invalid selection. Please try again.")

loop=1
while loop == 1:
    if mode == "1":
        manual()
    elif mode == "2":
        auto()
    elif mode == "3":
        randmode=choice(("1","2","3","4","5"))
        if randmode=="1":
            manual()
        else:
            auto()
