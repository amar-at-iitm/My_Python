"""
Q. A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
Write a program to detect these spams.

"""
print("This program will help you to identify spam comments")
comment = input("Please, Enter your comment: ")

spam = ["Make a lot of money", "buy now", "subscribe this", "click this"]
        
for x in spam: 
    if x in comment:
        print("This is a spam comment.")