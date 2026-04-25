import random

st = int(input("Enter Starting number : "))
end = int(input("Enter Ending number : "))

target = random.randint(st,end)     #use for generate random number 
# print(target)
while True:
    userChoise = (input("Guess a number or Quit(Q) : "))
    if(userChoise == "Q"):
        break

    userChoise = int(userChoise)
    if(userChoise == target):
        print("Correct Guess!!")
        break
    elif(userChoise < target):
        print("your choise is too small. choise big again ?")
    else:
        print("your choise is too big. choise small again ?")

print("----GAME OVER----")