import random
import time
score = 0
print ("Game activated in automatic mode. The game will now run without user interaction.")
while score < 5000:
    print ("Spinning...")
    time.sleep (random.uniform(0.5,3))
    spinningwheel = random.randint(1,12)
    print (spinningwheel)
    score = score+spinningwheel
    time.sleep (random.uniform(0.15,1))
    print ("Your score is now "+str(score)+".")
    time.sleep (random.uniform(1.2,4))
    jackpotchance = random.randint(0,19)
    if jackpotchance == 0:
        jackpotwinnings = random.randint (50, 1000)
        score = score+jackpotwinnings
        print ("Congratulations! You just won a jackpot of "+str(jackpotwinnings)+" points! This has been added to your score!")
        time.sleep(random.uniform(2.8,6))
        print ("Your score is now "+str(score)+".")
        time.sleep(random.uniform(1.2,4))
    if score >= 1000:
        print ("Well done! You've won the game with a score of "+str(score)+" points!")
        time.sleep(random.uniform(3.1, 7))
        score = 0
    monsterchance = random.randint(0,19)
    if monsterchance == 0:
        monstertake = random.randint(1, 1000)
        print ("Warning! Monster attack!")
        time.sleep(random.uniform(2.0, 4.0))
        while monstertake > 0:
            if score < 1:
                monstertake = -1
            else:
                print (random.choice(("Give me some points!", "Points! Points! Points!", "Give me some of those points, will ya?", "I love points", "Points are my friend", "I really want some points!", "Thanks for the points.", "Those points are all mine", "All mine!", "Hahahahaha!", "You're losing!", "Those points are mine! Mine! Mine!")))
                monstertake = monstertake - 1
                score = score - 1
                time.sleep(random.uniform(0.12, 0.3))
        print ("Your score is now "+str(score)+".")