# Importing modules
from random import randint
from random import randrange
from time import sleep
# Ask a user to type a number that will be used with the sleep function. Since we need an integer, we use int(input())
sleeptime=int(input("Welcome to the bingo caller script! Please type the number of seconds you want the script to wait to print a new number. Type 0 if you want to generate new numbers manually when you press the Enter key on your keyboard."))
if sleeptime>0:
    print("Automatic mode: on. The script will wait "+str(sleeptime)+" seconds before generating a new number.", end=" ")
elif sleeptime==0:
    print ("Automatic mode is turned off. Remember to press Enter to generate a new number.", end=" ")
else:
    print ("Error! Negative numbers are not allowed. Exiting...")
    exit()
input("Press Enter to continue.")
# Create a new, empty list called numberlist.
numberlist=[]
#A for loop ads numbers 1 through 75 to the list numberlist.
for x in range(1,76):
    # Using the append function to add x to the list.
    numberlist.append(x)
#Starting the while loop for the main part of the script.
calls=75
while calls>0:
    # Creating the inumber variable to be a random number between 0 and the length fo the numberlist list.
    inumber=randrange(0,len(numberlist))
    # Creating the bnumver variable to hold the element in numberlist indexed at inumber.
    bnumber=numberlist[inumber]
    #Remove the list item at index inumber from the list nubmerlist.
    numberlist.pop(inumber)
    # sets bletter to the appropriate letter based on bnumber.
    if bnumber <= 15:
        bletter="B"
    elif bnumber >= 16 and bnumber <= 30:
        bletter="I"
    elif bnumber >= 31 and bnumber <= 45:
        bletter="N"
    elif bnumber>=45 and bnumber <= 60:
        bletter="G"
    else:
        bletter="O"
    #Prints bletter+bnumber.
    print (bletter+str(bnumber))
    If the user chsoe automatic mode by typing a number grater than 0, then sleep for that amount of time in seconds, otherwise wait for the user to press the Enter key.
    if sleeptime>0:
        sleep(sleeptime)
    else:
        input("")
    calls=calls-1
print ("All numbers have been called out. The program will now exit.")