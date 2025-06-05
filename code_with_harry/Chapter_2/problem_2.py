# Write a python program to find remainder when a number is divided by z. 

def find_remainder(x, z):
    """
    This function returns the remainder when x is divided by z.
    
    :param x: The number to be divided
    :param z: The divisor
    :return: The remainder of x divided by z
    """
    return x % z    # In python, % operator gives the remainder


if __name__ == "__main__":
    print("Welcome to the Remainder Finder Program!")
    # Prompt the user for input
    a = int(input("Enter the number: "))
    b = int(input("Enter the divisor: "))

    # Call the function and print the result
    reminder = find_remainder(a, b)
    print(f"The remainder when {a} is divided by {b} is: {reminder}")

    # Thank the user for using the program
    print("Thank you for using the program!")