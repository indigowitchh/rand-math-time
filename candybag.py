import random

candybag = [0, 0, 0, 0, 0, 0]

num = random.randrange(0,100)

def candies():
    numBars = random.randrange(1,5)
    num = random.randrange(0,100)
    if num < 15:
        print("You got", numBars, "butterfinger!")
        candybag[0]+= numBars
    elif num < 35:
        print("You got" , numBars,  "hersheys!")
        candybag[1]+= numBars
    elif num < 70:
        print("You got" , numBars, "PB cup!")
        candybag[2]+= numBars
    elif num < 80:
        print("You got" , numBars,  "mnms!")
        candybag[3]+= numBars
    elif num < 98:
        print("You got", numBars, "sour patch kids!")
        candybag[4]+= numBars
    else:
        print("You got a rock.")
        candybag[5]+= 1
    
candies()
candies()
candies()
candies()
candies()

print("Your candybag is now:", candybag)
