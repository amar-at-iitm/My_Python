"""
Q. Write a python function to print first n lines of the following pattern: 
*** 
**               - for n = 3 
* 

"""

def print_star(n=3):
    for i in range(n,0,-1):
        print(i*"*")


if __name__=="__main__":
    print("This program will print the starts")
    print_star()