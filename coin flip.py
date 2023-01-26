import random 

def coin_flip(k,side):
    count = 0
    while count != k:
        i = random.randint(0, 1)
        #0 = H
        if i == 0: 
            print("H", end=" ")
            if side == "H":
                count +=1
            if side == "T" and count > 0:
                count = 0
        #1 = T
        else: 
            print("T", end=" ")
            if side == "T":
                count +=1
            if side == "H" and count > 0:
                count = 0
    print()
    print("You got " + str(side) + " " + str(k) + " times in a row!")
    



