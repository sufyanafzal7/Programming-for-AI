sNum = int(input("Enter starting number: "))
eNum = int(input("Enter ending number: "))
sum = 0
for i in range(sNum,eNum+1):
    sum = sum +i

print(f"The sum is {sum}")