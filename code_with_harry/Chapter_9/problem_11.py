#  Write a python program to rename a file to “renamed_by_ python.txt.

import os

def rename_file(file_name, new_name="renamed_by_python.txt"):

    with open(file_name,"w") as f:
     f.write(f"Renaming old file name '{file_name}' to '{new_name}")

    os.rename("file_to_rename.txt", "renamed_by_python.txt")
    print(f"The file '{file_name}' is ranamed to '{new_name}' and saved successfully")


if __name__=="__main__":
   
    print("This programe will rename ta file in existing directory")
    file_name = input("Eneter the file name: ")
    new_name = input("Enter the new name(default=renamed_by_python.txt): ")
    rename_file(file_name, new_name)
