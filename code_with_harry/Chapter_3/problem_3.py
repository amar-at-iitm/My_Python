# Write a program to detect double space in a string.

string = input("Enter a string: ")
if "  " in string:
    print("Double space detected")
else:
    print("No double space detected")