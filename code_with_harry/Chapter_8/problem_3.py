"""
Q. How do you prevent a python print() function to print a new line at the end.
Ans: we can prevent the print() function in Python from printing a new line at the end 
by using the 'end' parameter. By default, end is set to '\n' (the newline character).
we can change it to an empty string or any other character we prefer.

"""
print("This is the first part of a line,", end='')
print("and this is 2nd part of the same line.")