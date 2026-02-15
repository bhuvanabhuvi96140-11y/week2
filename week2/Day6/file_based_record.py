def add_record():
    file = open("students.txt", "a")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    file.write(roll + "," + name + "," + marks + "\n")
    file.close()
    print("Record added successfully!\n")
def view_records():
    try:
        file = open("students.txt", "r")
        print("\nStudent Records:")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print("Roll:", roll, "| Name:", name, "| Marks:", marks)
        file.close()
    except FileNotFoundError:
        print("No records found!\n")
def search_record():
    roll_search = input("Enter Roll Number to search: ")
    found = False
    try:
        file = open("students.txt", "r")
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print("Record Found:")
                print("Name:", name)
                print("Marks:", marks)
                found = True
                break
        file.close()
        if not found:
            print("Record not found!")
    except FileNotFoundError:
        print("No records found!\n")
while True:
    print("\n===== File Based Record System =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_record()
    elif choice == '2':
        view_records()
    elif choice == '3':
        search_record()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")