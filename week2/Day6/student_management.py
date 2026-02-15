students = {}
roll = input("Enter Roll Number: ")
name = input("Enter Name: ")
marks = input("Enter Marks: ")
students[roll] = {"Name": name, "Marks": marks}
print("\nStudent Details:")
for roll, details in students.items():
    print("Roll Number:", roll)
    print("Name:", details["Name"])
    print("Marks:", details["Marks"])