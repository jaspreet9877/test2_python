phoneDirectory = {}

def mainMenu():
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY\n")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit")

def ADDRECORD():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phoneDirectory[name] = phone
    print(name, "added to the phone directory with phone number", phone)

def SEARCHRECORD():
    name = input("Enter name to search: ")
    if name in phoneDirectory:
        print("Phone number of", name, "is", phoneDirectory[name])
    else:
        print(name, "not found in the phone directory")

def UPDATERECORD():
    name = input("Enter name to update: ")
    if name in phoneDirectory:
        phone = input("Enter new phone number: ")
        phoneDirectory[name] = phone
        print(name, "phone number updated to", phone)
    else:
        print(name, "not found in the phone directory")

def DELETERECORD():
    name = input("Enter name to delete: ")
    if name in phoneDirectory:
        del phoneDirectory[name]
        print(name, "deleted from the phone directory")
    else:
        print(name, "not found in the phone directory")

mainMenu()

while True:
    choice = input("\nEnter your choice: ")
    if choice == '1':
        ADDRECORD()
    elif choice == '2':
        SEARCHRECORD()
    elif choice == '3':
        UPDATERECORD()
    elif choice == '4':
        DELETERECORD()
    elif choice == '5':
        print("\nThank you !!")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")

