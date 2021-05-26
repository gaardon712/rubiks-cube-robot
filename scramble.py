import random

def scramb():
    scram = []
    for i in range(12):
        x = random.randint(1,19)
        if(x == 1):
            scram.append("W")
        if(x == 2):
            scram.append("W'")
        if(x == 3):
            scram.append("G")
        if(x == 4):
            scram.append("G'")
        if(x == 5):
            scram.append("R")
        if(x == 6):
            scram.append("R'")
        if(x == 7):
            scram.append("B")
        if(x == 8):
            scram.append("B'")
        if(x == 9):
            scram.append("O")
        if(x == 10):
            scram.append("O'")
        if(x == 11):
            scram.append("Y")
        if(x == 12):
            scram.append("Y'")
        if(x == 13):
            scram.append("Y2")
        if(x == 14):
            scram.append("W2")
        if(x == 15):
            scram.append("R2")
        if(x == 16):
            scram.append("G2")
        if(x == 17):
            scram.append("B2")
        if(x == 18):
            scram.append("O2")
    return(scram)
