# Write a program to make a copy of a text file “this. txt” 

def make_copy(file):
    with open(file,"r") as f:
        content = f.read()
        
    new_name = f"copy_{file}"

    with open(new_name,"w") as f_copy:
        f_copy.write(content)
        print(f"{file} is copied to {new_name}")



if __name__=="__main__":
    print("This program will copy a given file ")

    # Taking file name from the user as input
    file = input("Enter the name of file to copy: ")
    
    # calling the function
    make_copy(file)
   