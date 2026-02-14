with open("students.txt", "a") as file:
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    file.write(roll + "," + name + "," + marks + "\n")
print("Student record stored successfully.")
