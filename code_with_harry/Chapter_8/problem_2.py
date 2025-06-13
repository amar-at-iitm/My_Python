# Write a python program using function to convert Celsius to Fahrenheit.

def cel_2_far(c):
    # The formula to convert Celsius to Fahrenheit is: F = (C * 9/5) + 32
    f = (c*(9/5))+32
    f = round(f,2)
    return f


if __name__=="__main__":
    print("This program will convert celius to fahrenheit")
    c = float(input("Enter the tempreture in Celsius(only number): "))
    f = cel_2_far(c)
    print(f"The tempreture in Fahrenheit is {f}°F")