# Write a python program to calculate the square of a number entered by the user.

# Function to calculate the square of a number
def calculate_square(number):
    """Calculate the square of a number."""
    return number ** 2  


if __name__ == "__main__":
    print("Welcome to the Square Calculation Program!")
    
    # Asking the user to input a number
    number = eval(input("Enter a number: "))
    
    # Calculating the square
    square = calculate_square(number)
    
    # Displaying the result
    print(f"The square of {number} is: {square}")
    
    # Thanking the user for using the program
    print("Thank you for using the program!")