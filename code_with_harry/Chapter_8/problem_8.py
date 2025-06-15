# Write a python function to print multiplication table of a given numbe


def mult_table(n):
    for i in range(10):
        print(n*(i+1))



print("This program will print multiplication table using function")
n = int(input("Enter the number: "))
# Calling the function
mult_table(n)