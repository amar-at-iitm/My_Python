# Write a program to find the sum of first n natural numbers using while loop

print("This program will find the sum of first n natural number")

n = int(input("Enter a natural number: "))

sum = 0 
i = 1
while i < (n+1):
    sum += i
    i+=1


print(f"Sum of first {n} number is {sum}")