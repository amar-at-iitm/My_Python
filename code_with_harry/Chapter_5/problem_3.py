""""
Q. Can we have a set with 18 (int) and '18' (str) as a value in it?
Ans: Yes, because set is a collection of unique elements, where elements can be any type.
In this case, int 18, and str '18' will be treated as different elements.

Below is code showing this. Run this code to verify.
"""
s = set()
num = int(input(" Enter a number as int : "))
s.add(num)
print(" Set after adding an int: ",s)
str = input(" Enter a number as string : ")
s.add(str)
print("Set after adding number as string : ", s )