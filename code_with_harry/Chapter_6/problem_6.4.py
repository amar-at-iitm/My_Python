# Write a program to find whether a given username contains less than 10 characters or not. 
print("This program will check the lenght of username")
U_name = input("Enter your username: ")
l = len(U_name)
if l>10:
    print("This username contains more than 10 characters")
elif l == 10:
    print("This username contains exactly 10 characters")
else: 
    print("This username contains less than 10 characters")