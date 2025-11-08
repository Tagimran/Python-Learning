def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!")

def view_contacts():
    with open("contacts.txt", "r") as f:
        print("\nAll Contacts:")
        for line in f:
            name, phone, email = line.strip().split(",")
            print(f"Name: {name} | Phone: {phone} | Email: {email}")

while True:
    print("\n=== Contact Book ===")
    print("1. Add\n2. View\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid input, try again.")

