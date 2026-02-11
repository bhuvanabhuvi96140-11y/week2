student = {
    "Name": "Bhuvana",
    "Age": 22,
    "Course": "MCA"
}
print("Original Dictionary:")
print(student)
student["City"] = "Shivamogga"
print("\nAfter Adding City:")
print(student)
student["Age"] = 23
print("\nAfter Updating Age:")
print(student)
del student["Course"]
print("\nAfter Deleting Course:")
print(student)
