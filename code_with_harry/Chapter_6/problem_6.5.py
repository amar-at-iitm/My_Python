# Write a program which finds out whether a given name is present in a list or not. 

name_list = ["amar", "anvit", "aiswajit", "briti", "devesh", "divyanshu"]

print("This programe will help you to check weather your name is in the list or not")

name = input( "Please Enter Your Name: ")
name2 = name.capitalize()
print(name2)


name = name.lower()
if name in name_list:
    print("Yes, Your name is in the list")
else: 
    print( "Sorry, Your name is not in the list")