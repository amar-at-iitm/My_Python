#  Write a python program to rename a file to “renamed_by_ python.txt.

import os


print("This file will rename the existing '.txt' file")

with open("file_to_rename.txt","w") as f:
    f.write("Renaming old file name 'file_to_rename' to 'renamed_by_python.txt")

os.rename("file_to_rename.txt", "renamed_by_python.txt")
print("The file 'file_to_rename.txt' is ranamed to 'rename_by_python.txt' and saved successfully")