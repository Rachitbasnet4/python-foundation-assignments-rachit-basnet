'''
Stretch Exercise: Contact Book Menu
Name: Rachit Basnet
Day 2
'''

# empty dictionary 
contacts = {}

# using while loop to keep runnning the program
while True:

    # Displaying the menu
    print("\nContact Book")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contact")
    print("5. Exit")

    # taking user choice
    choice = int(input("Enter your choice: "))

    # 1. Add contact
    if choice == 1:
        name = input("Enter name: ").title()
        phone = int(input("Enter phone number: "))
        email = input("Enter email address: ").lower()

        # adding contact details in a nested dictionary
        contacts[name]={
            "Phone number": phone,
            "Email address": email
        }

        # output: displaying success message 
        print("Contact added successfully.")

    # 2. Search contact
    elif choice == 2:
        name = input("Enter name: ").title()

        # output using condition to look into contact dict and displaying output
        if name in contacts:
            print(f"Name:{name}")
            print(f"Phone number: {phone}")
            print(f"Email address: {email}")
        else:
            print("Contact not found. Please search again")

    # 3. Delete contat
    elif choice == 3:
        name = input("Enter name: ").title()

        # output using condition to delete contact and displaying output
        if name in contacts:
            del contacts[name]
            print("Conact deleted sucessfully.")
        else:
            print("Contact not found. Please try again.")
    # 4. Display all contact
    elif choice == 4:
        if len(contacts) == 0:
            print("No contact found.")
        else:
            print("\nAll Contact:")

            # looping through contacts dict and showing all contact details
            for name, details in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['Phone number']}")
                print(f"Email: {details['Email address']}")
                print()

    # 5. Exit
    elif choice == 5:
        print("Exiting contact book...")

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select 1-5.")
