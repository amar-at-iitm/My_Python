# Write a program to find out whether a file is identical & matches the content of another file.

def similarity_checker(file_1, file_2):
   with open(file_1, "r") as f1: 
      content_1 = f1.read()
      with open(file_2,"r") as f2:
         content_2 = f2.read()
         if content_1 == content_2:
            print("Both files have the same content") 
         else:
            print("Both files have different content")




if __name__=="__main__":
    print("This program will help you to find similarity between two program")

    file_1 = input("Enter the name of 1st file : ")
    file_2 = input("Enter the name of 2nd file : ")
    
    # calling the function
    similarity_checker(file_1, file_2)
