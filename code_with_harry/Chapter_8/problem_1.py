# Write a program using functions to find greatest of three numbers.

def greatest_of_three():
    l = []
    for i in range(3):
        n = float(input(f"Enter number{i+1}: "))
        l.append(n)

    # m = 0
    for x in l:
        if x>n:
            n=x
    print(f"Greatest number among these three numbers are {n}")

if __name__== "__main__":
    print("This program will find the greatest number among three given numbers")
    greatest_of_three()