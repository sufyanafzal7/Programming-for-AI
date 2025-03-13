num = int(input("Enter number: "))

flag = True

for i in range(2,num):
    if(num%i==0):
        flag = False

if(flag==True):
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is not prime.")