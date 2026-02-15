try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Problem reading the file.")