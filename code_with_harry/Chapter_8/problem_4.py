# Write a recursive function to calculate the sum of first n natural numbers. 

def first_n_sum(n):
    if n==1:
        return 1
    else:
        return n + first_n_sum(n-1)

if __name__=="__main__":
    print("This program will give sum of firsr n natural number using recursion")
    n = int(input("Enter a natural number: "))
    s = first_n_sum(n)
    print(f"The sum of first {n} natural number is {s}")