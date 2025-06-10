"""
Q. Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 - 100 => Ex 
80 - 90  => A 
70 - 80  => B 
60 - 70  => C 
50 - 60  => D 
<50      => F
"""

from problem_2 import mark_collector, percent_mark
def grading_scheme(a):
    
    if 90<=a:
        grade = "Ex"
    elif 80<=a<90:
        grade = "A"
    elif 70<=a<80:
        grade = "B"
    elif 60<=a<70:
        grade = "C"
    elif 50<=a<60:
        grade = "D"
    else:
        grade = "F"

    return grade

if __name__ == "__main__":

    print( " Welcome!\nThis program will help you to find out your grade ")
    name = input( "Please Enter your name : ")
    print(f" Dear {name}, Please enter the following details ")

    n,obt_mark, full_mark = mark_collector()
    avg, _, _ = percent_mark(n,obt_mark, full_mark)

    grade = grading_scheme(avg)

    if grade == "F":
        print(f"Sorry, You gor "F" grade")
    else: 
        print(f"Congratulations, You got {grade} grade.")