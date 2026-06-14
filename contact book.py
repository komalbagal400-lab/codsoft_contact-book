# Contact Management System

contacts = []

while True:
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })

        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    # Search Contact
    elif choice == "3":
        search = input("Enter Name or Phone Number: ")
        found = False

        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter Name to Update: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("New Phone: ")
                contact["email"] = input("New Email: ")
                contact["address"] = input("New Address: ")
                print("Contact updated successfully!")
                found = True

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")