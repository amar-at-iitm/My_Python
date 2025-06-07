# Write a program to sum a list with 4 numbers.
num = []
sum = 0
for i in range(4):
    a = float(input(f" Enter the number {i+1} : "))
    num.append(a)

for x in num:
    sum+=x

print("sum of these four numbers are : ", sum )