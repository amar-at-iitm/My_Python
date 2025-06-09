"""
Q2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user
"""

obt_mark = []
full_mark = []

print( " Welcome!\nThis program will help you to find out weather you passed or not ")
name = input( "Please Enter your name : ")
print(f" Dear {name}, Please enter the following details ")

n = int(input(" Enter the number of courses you have taken: "))

for i in range(n):
    om = float(input(f"Enter the marks obtained in subject {i+1}: "))
    fm = int(input(f"Enter the full marks for subject {i+1}: "))
    obt_mark.append(om)
    full_mark.append(fm)

indv_perc = []
for i in range(n):
    p = (obt_mark[i]/full_mark[i])*100
    indv_perc.append(p)
m = 0
s = 0
for x in indv_perc:
    s = s + x
    if x < 33:
        m +=1

if m == 1:
    print(f"Sorry! You failed in the examination, because you are below 33% in {m} subject")
    

if m > 1:
    print(f"Sorry! You failed in the examination, because you are below 33% in {m} subjects")

if m == 0:
    avg = s/4
    if avg < 40:
        print(f"Sorry! You failed in the examination,\nthough you got more than 33% in each subject, but you are <40% in overall")
    else:
        print(f"Congratulations {name}, You sucessfully passed the examination")