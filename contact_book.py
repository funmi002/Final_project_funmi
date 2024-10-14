#Contact book
contacts = {}
while True: 
    print("\n1. Add contact")
    print("2.Delete contact")
    print("3.View contacts")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Name: ")
        if name in contacts: del contacts[name]
    elif choice == "3": 
        for name, phone in contacts.items(): print(f"{name}: {phone}")
    elif choice == "4":     
            break
    else: 
        print("invalid choice.")
