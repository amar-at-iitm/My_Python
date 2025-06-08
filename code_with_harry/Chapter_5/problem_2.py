# Write a program to input eight numbers from the user and display all the unique numbers (once).

num = set()

for i in range(8):
    n = input( f"Enter the number : ")
    num.add(n)

print("All the unique numbers are : ")

for n in num:
    print(n)