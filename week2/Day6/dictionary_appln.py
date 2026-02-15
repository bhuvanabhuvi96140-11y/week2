dictionary = {}
while True:
    print("\n===== Dictionary Application =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Word")
    print("4. Delete Word")
    print("5. Display All Words")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        word = input("Enter word: ")
        meaning = input("Enter meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")
    elif choice == '2':
        word = input("Enter word to search: ")
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found!")
    elif choice == '3':
        word = input("Enter word to update: ")
        if word in dictionary:
            meaning = input("Enter new meaning: ")
            dictionary[word] = meaning
            print("Word updated successfully!")
        else:
            print("Word not found!")
    elif choice == '4':
        word = input("Enter word to delete: ")
        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully!")
        else:
            print("Word not found!")
    elif choice == '5':
        if dictionary:
            print("\nDictionary Words:")
            for word, meaning in dictionary.items():
                print(word, ":", meaning)
        else:
            print("Dictionary is empty!")
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")