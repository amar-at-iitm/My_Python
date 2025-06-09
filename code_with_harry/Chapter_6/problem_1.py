# Write a program to find the greatest of four numbers entered by the user.
num = []


for i in range(4):
    n = float(input(f"Enter the number {i+1}: "))
    num.append(n)

m = 0 
for x in num:
    if x > m:
        m = x

print( f"The greatest number among these four numbers is : {m}")