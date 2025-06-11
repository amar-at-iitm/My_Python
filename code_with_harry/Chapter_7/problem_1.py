# Write a program to print multiplication table of a given number using for loop.
print("This program will print the table of a number")

n = int(input("Enter a number: "))
print(f"Table of {n} is : ")
for i in range(10):
    print(n*(i+1))