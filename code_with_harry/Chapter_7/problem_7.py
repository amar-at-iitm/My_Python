"""
Q. Write a program to print the following star pattern. 
  * 
 *** 
*****  for n = 3 

"""

n = 3

for i in range(n):
    print((n-i)*" "+((2*i)+1)*"*"+(n-i)*" ")