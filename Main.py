from Display import Contact
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def display(self):
        if not self.contacts:
            print("No contact found")
        else:
            print("List of all contacts:",'\n')
            for name, contact in self.contacts.items():
                print("Name:", name)
                print("Phone:", contact.phone)
                print("Email:", contact.email,'\n')

    def add_contact(self, contact):
          self.contacts[contact.name] = contact
Contact_Book = ContactBook()
while True:
    print("Enter 1 to add a new contact")
    print("Enter 2 to display all contacts")
    print("Enter 3 to exit")

    choice = int(input("Enter your choice:"))
    print("                                ")
    if choice == 1:
        name = input("Enter the name:")
        phone = input("Enter phone number:")
        email = input("Enter the email address:")
        contact = Contact(name,phone,email)
        Contact_Book.add_contact(contact)
        print("Contact added",'\n')
    elif choice == 2:
        Contact_Book.display()
    elif choice == 3:
        print("Exiting...")
        break
    else:
         print("Invalid choice")