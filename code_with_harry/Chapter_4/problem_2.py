# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    mark = float(input( f"Enter marks of Student {i+1}: "))
    marks.append(mark)


marks.sort()

print(" The Marks of the students are in sorted manner")

for mark in marks: 
    print(mark)