from time import sleep
from random import uniform
from random import randrange
ascore=0
bscore=0
ahealth=500
bhealth=500
dlevel=2
hlevel=3
def greset():
    global ahealth
    global bhealth
    global dlevel
    global hlevel
    ahealth=500
    bhealth=500
    dlevel=2
    hlevel=3

def mattack():
    #Use the global keyword if you want to use global variables within a function.
    global ahealth
    global bhealth
    global dlevel
    global hlevel
    you=input("Please press Enter to attack, or press S then enter to check your status.")
    if you=="s":
        print ("Your status is as follows: You currently have "+str(ahealth)+" health, and you're apponent has "+str(bhealth)+" health.")
    elif you=="":
        print ("Attack")
        sleep(uniform(0.300000,1.300000))
        damage=(randrange(1,dlevel))
        bhealth=bhealth-damage
        print (str(damage)+" damage. The computer has "+str(bhealth)+" health remaining.")
        sleep(uniform(3.000000,4.000000))
        levelchance=randrange(1,3)
        if levelchance==1:
            dlevel=dlevel+1
            print ("Level up! You and the computer can cause more damage per attack.")
            sleep(uniform(4.000000,5.000000))
        difficultchance=randrange(1,11)
        if difficultchance==1:
            hlevel=hlevel+1
            print ("Difficulty level changed! The computer will attack more often.")
            sleep(uniform(4.000000,5.000000))
    else:
        print ("Invalid command. Pleas try again.")
        sleep(uniform(2.500000,3.200000))
        mattack()
def cattack():
    global ahealth
    global bhealth
    global dlevel
    global hlevel
    print ("The computer attacks you.")
    sleep(uniform(1.500000,2.300000))
    damage=randrange(1,dlevel)
    ahealth=ahealth-damage
    print (str(damage)+" damage. You have "+str(ahealth)+" health remaining.")
    sleep(uniform(2.500000,3.500000))
    levelchance=randrange(1,3)
    if levelchance==1:
        dlevel=dlevel+1
        print ("Level up! You and the computer can cause more damage per attack.")
        sleep(uniform(4.000000,5.000000))
    difficultchance=randrange(1,11)
    if difficultchance==1:
        hlevel=hlevel+1
        print ("Difficulty level changed! The computer will attack more often.")
        sleep(uniform(4.000000,5.000000))
gamecheck=True
while gamecheck==True:
    while ahealth>0 and bhealth>0:
        chance=randrange(1,hlevel)
        if chance == 1:
            mattack()
        else:
            cattack()
    if ahealth<=0:
        bscore=bscore+1
        print ("The computer wins the game. Wins: "+str(ascore)+" losses: "+str(bscore))
    else:
        ascore=ascore+1
        print("Congratulations! You won this game! Wins: "+str(ascore)+" Losses: "+str(bscore))

    questionloop=True
    while questionloop==True:
        question=input("Game over! Would you like to start the game over? Type Y or N.")
        if question=="y":
            greset()
            questionloop=False
        elif question=="n":
            gamecheck=False
            print ("Exiting game.")
            questionloop=False
        else:
            print ("Invalid command. Please try again.")