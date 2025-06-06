# Write a python program to find an average of two numbers entered by the user


# Function to calculate the average of two numbers
def calculate_average(num1, num2):
    """Calculate the average of two numbers."""
    return (num1 + num2) / 2


if __name__ == "__main__":
    print("Welcome to the Average Calculation Program!")
    
    # Asking the user to input two numbers
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    
    # Calculating the average
    average = calculate_average(num1, num2)
    
    # Displaying the result
    print(f"The average of {num1} and {num2} is: {average}")
    
    # Thanking the user for using the program
    print("Thank you for using the program!")