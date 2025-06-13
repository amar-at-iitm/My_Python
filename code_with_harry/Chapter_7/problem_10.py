# Write a program to print multiplication table of n using for loops in reversed order.

print("This program will print multiplication table in reverse order using for loop")

n = int(input("Enter a number: "))

print(f"Multiplication table of {n} in reverse order: ")
for i in range(10,0,-1):
    print(i*n)