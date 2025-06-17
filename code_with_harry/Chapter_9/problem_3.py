"""
Q. Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13year old. 
"""

import os
# Create the directory if it doesn't exist
os.makedirs("mult_table",  exist_ok = True)

for i in range(2,21):
    f_name = f"table_{i}.txt"      # Different file name for each table
    file_path = os.path.join("mult_table", f_name)

    with open(file_path, "w") as f:
        f.write(f"Multiplication Table of {i}\n")
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")      # Writing table in structured format