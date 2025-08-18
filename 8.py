import random
target=random.randint(1,100)
while True:
    userinput=input("guess the number or quit(Q)")
    if userinput=="Q":
        break
    userinput=int(userinput)
    if(target==userinput):
        print("your guess is correct")
        break
    elif(target<userinput):
        print("your guess is high")
    else:
        print("your guess is low")