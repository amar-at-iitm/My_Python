#  Write a program to wipe out the content of a file using python.

def wipe_content(file_name):

    with open(file_name,"w") as f:
        pass  # Opening in "w" mode already truncates the file

    print(f"Successfully wiped out all the content of {file_name}")



if __name__== "__main__":
    print("This program will wipe out all the contents of a file in existing directory ")

    file_name = input("Enter the file name: ")
    wipe_content(file_name)