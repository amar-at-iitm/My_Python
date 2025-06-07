# Write a program to count the number of zeros in the following tuple: 
# a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)

count = 0

for x in a :
    if x==0:
        count += 1

print ( f" Number of zeros in a is : {count}")
