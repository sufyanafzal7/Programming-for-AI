import random

ranNum = random.randint(0,9)

track = 0
num = input("Enter number: ")

while(num!="exit"):
    n = int(num)
    if(n == ranNum):
        track+=1
        print(f"You guessed the number {ranNum}")
        print("Enter \"exit\" to exit the program.")
    elif(n > ranNum):
        track+=1
        print("Too high")
    elif(n < ranNum):
        track+=1
        print("Too low")
    num = input("Enter number: ")



print(f"Track of guessing numbers {track}")