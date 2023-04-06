
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone
class Contact_Book:
    def __init__(self):
        self.contacts = {}
    def display(self):
        if not self.contacts:
            print("no contact found")
        else:
            print("list of all contacts")
            for name, contact in self.contacts.items():
                print("Name:", name, end='')
                print("Phone:", contact.phone, end='')
                print("Email:", contact.email)
                print("----------------------")

