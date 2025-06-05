# Check the type of variable assigned using input () function. 

# Function to detect the type of input variable
def detect_input_type(a):
    if isinstance(a, int):
        return "int"
    elif isinstance(a, float):
        return "float"
    elif isinstance(a, complex):
        return "complex"
    elif isinstance(a, str):
        return "str"
    elif isinstance(a, bool):
        return "bool"
    elif isinstance(a, list):
        return "list"
    elif isinstance(a, tuple):
        return "tuple"
    elif isinstance(a, dict):
        return "dict"
    elif isinstance(a, set):
        return "set"
    else: 
        return "unknown type"


if __name__ == "__main__":
    print("Welcome to the Type Checker Program!")
    # Taking input from the user to check its type
    a = eval(input("Enter a value: "))    


    # Calling the function to detect the type of 'a'
    input_type = detect_input_type(a)
    # Displaying the type of the variable 'a'
    print(f"The type of the variable 'a' is: {input_type}")
    # Thanking the user for using the program
    print("Thank you for using the program!")



#////////////////////////////////////////////////////////////////////////////////
# print("Welcome to the Type Checker Program!")

# # Taking input from the user to check its type
# a = input("Enter a value: ")

# # Displaying the type of the variable 'a'
# print(f"The type of the variable 'a' is: {type(a)}")

# # Thanking the user for using the program
# print("Thank you for using the program!")