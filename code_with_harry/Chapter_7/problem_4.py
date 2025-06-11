# Write a program to find whether a given number is prime or not.

print("This program will help you to check prime number")

n = int(input("Enter the number: "))

for i in range(2,(n//2)+1):
    if n%i== 0:
        print(f"{n} is not a prime number")
        quit()

print(f"{n} is a prime number")