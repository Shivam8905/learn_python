import random
randNo = random.randint(1,3)
you = int(input("Enter 1 for Stone, 2 for Paper and 3 for Scissor ->"))

def game(randNo, you):
    if(you==1):
        if(you==1 and randNo==3):
            return 1
        elif(you==1 and randNo==2):
            return -1
        else:
            return 0
    elif(you==2):
        if(you==2 and randNo==1):
            return 1
        elif(you==2 and randNo==3):
            return -1
        else:
            return 0
    elif(you==3):
        if(you==3 and randNo==2):
            return 1
        elif(you==3 and randNo==1):
            return -1
        else:
            return 0

n = game(randNo, you)
if(n==1):
    print("You won")
elif(n==-1):
    print("You loss")
else:
    print("It's a draw")

list = ["Stone", "Paper", "Scissor"]
print("Because You choose " + str(list[you-1]) + " and Machine choose " + str(list[randNo-1]))