# Write a python program to print the contents of a directory using the os module.

import os
# This code prints the contents of the current directory
current_directory = os.getcwd()
print(f"Contents of the directory '{current_directory}':")
for item in os.listdir(current_directory):
    print(item) 