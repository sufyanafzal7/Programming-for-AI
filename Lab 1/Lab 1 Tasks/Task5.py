num = int(input("Enter number: "))

factorial = 1

for i in range(num, 0, -1):
    factorial *= i

print(f"Factorial is {factorial}")
