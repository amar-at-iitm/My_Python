# Write a python program to add two numbers.

def add_two_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    
    :param num1: First number
    :param num2: Second number
    :return: Sum of num1 and num2
    """
    return num1 + num2

if __name__ == "__main__":
    # Take input from the user
    print("Welcome to the addition program!")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    # Call the function to add the two numbers
    sum = add_two_numbers(a, b)
    print(f"The sum of {a} and {b} is: {sum}")
    
    # Thank the user for using the program
    print("Thank you for using the addition program!")