# Write a python function to remove a given word from a list ad strip it at the same time.
"""
The strip() function in Python is used to remove leading and 
trailing whitespace (like spaces, tabs, or newline characters) from a string.
"""
def remove_and_strip(list, tgt_word):
    r_list = []
    for word in list:
        striped_word = word.strip()
        if striped_word != tgt_word:
            r_list.append(striped_word)

    return r_list


words = ["  apple", "banana ", " orange", "apple ", "grape"]
print(remove_and_strip(words, "apple"))