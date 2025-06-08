# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.


dict = {}

for i in range(1):
    print(f"                   For Friend {i+1}: ")
    name = input( "             Enter Your Name: ")
    lang = input("Enter Your Favourite Language: ")
    dict[name] = lang

print( " Name     Favorite_language")
for x in dict.keys():
    print(f" {x}           {dict[x]}")
