# Write a python function which converts inches to cms. 


def inch_2_cm(n):
    return 2.54*n

print("This program will convert inches to centimeters")
n = float(input("Enter the measurement in inches: "))
c = inch_2_cm(n)
print(f"Now the measurement is {c}cm.")