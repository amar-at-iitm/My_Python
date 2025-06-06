#    Use comparison operator to find out whether ‘a’ given variable a is greater than 
#   ‘b’ or not. Take a = 34 and b = 80


# Function to compare two numbers
def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"
    
if __name__ == "__main__":
    print("Welcome to the Number Comparison Program!")
    
    # Asking the user to input two numbers is not needed as we are using fixed values.
    print(" If you want to enter your own numbers, press Y otherwise press N to use default values.")
    user_choice = input("Enter your choice (Y/N): ").strip().upper()
    if user_choice == 'Y':
        # Taking input from the user for a and b
        a = eval(input("Enter the value for a: ")) 
        b = eval(input("Enter the value for b: "))
    else:
        print("Using default values for a and b.")
        # Assigning values to a and b
        a = 34
        b = 80
    
    # Calling the function to compare a and b
    result = compare_numbers(a, b)
    
    # Displaying the result of the comparison
    print(result)
    
    # Thanking the user for using the program
    print("Thank you for using the program!")