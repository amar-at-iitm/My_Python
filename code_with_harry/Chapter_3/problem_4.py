# Replace the double space from problem 3 with single spaces.

from problem_3 import string

string2 = string.replace("  ", " ")
print("String after replacing double spaces with single spaces:\n", string2)

while "  " in string:
    string = string.replace("  ", " ")
print("String after replacing double spaces with single spaces using while loop:\n", string)