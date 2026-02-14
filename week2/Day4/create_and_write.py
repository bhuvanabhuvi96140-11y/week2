import os
filename = "sample.txt"
if os.path.exists(filename):
    print("File exists.")
    file = open(filename, "a")  
    file.write("\nThis line is added to the existing file.")
else:
    print("File does not exist. Creating new file.")
    file = open(filename, "w")   
    file.write("This is a new file created.")
file.close()
print("Operation completed successfully.")