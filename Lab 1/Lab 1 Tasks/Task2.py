num = input("Enter number: ")
sumE = 0
sumO = 0

n = num

for i in num:
    if int(i)%2 == 0:
        sumE = sumE+int(i)
    else:
        sumO = sumO + int(i)


print(f"The number is: {num}")
print(f"Sum of Even: {sumE}")
print(f"Sum of Odd: {sumO}")
