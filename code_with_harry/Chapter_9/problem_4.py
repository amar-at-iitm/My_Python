"""
Q. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.

"""

def replace_word(file_name, word="Donkey"):
    
    with open(file_name) as f:
        content = f.read()    
        parts = content.split(word)
        
        # Keep the first instance, replace the rest
        new_content = parts[0] + word + "#####".join(parts[1:])
        
        # Write the updated content back to the file
        with open(file_name, "w") as f:
            f.write(new_content)

        print(f"All occurrences of '{word}' except the first have been replaced with '#####'.")


if __name__=="__main__":
    print("This program will replace from a file( default = 'Donkey')")

    file_name = input("Enter the file name: ")
    word = input("Enter the word to be replaced by ##### : ")

    replace_word(file_name, word)