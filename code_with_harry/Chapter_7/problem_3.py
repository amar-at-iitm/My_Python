# Write a program to print multiplication table of a given number using while loop.

print("This program will print the table of a number using \'while loop\'")

n = int(input("Enter a number: "))
print(f"Table of {n} is : ")
i = 1
while i<11:
    print(n*(i))
    i+=1