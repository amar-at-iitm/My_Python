# Write a program to calculate the factorial of a given number using for loop.

print("This programe will calculate the factorial of a given number")

n = int(input("Enter the nuber: "))

f = 1

if n < 0:
    print("Enter a number >= 0")
else:
    for i in range(1,n+1):
        f = f*i
    print(f"The value of {n}! = {f}")


