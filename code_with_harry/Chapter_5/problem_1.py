# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

dict = {"sev":"apple",
        "gend":"ball",
        "billi":"cat",
        "kutta":"dog"}

hindi_word = input("Enter the word to search : ")

print(f"Hindi       English\n {hindi_word}         {dict[hindi_word]}")