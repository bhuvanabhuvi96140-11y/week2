class AgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeError("You must be 18 or older.")
    print("Access granted.")
except AgeError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input! Please enter a number.")