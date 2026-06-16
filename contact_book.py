"""
ContactBook Class — Week 4 OOP Practice
Demonstrates: classes, list of dictionaries,
              searching, methods
"""

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        """Add a new contact to the book."""
        contact = {"name": name, "phone": phone}
        self.contacts.append(contact)
        print(f" Contact '{name}' saved!")

    def show_contacts(self):
        """Display all saved contacts."""
        if len(self.contacts) == 0:
            print(" No contacts yet.")
        else:
            print(f"📒 Contact Book ({len(self.contacts)} contacts):")
            print("-" * 30)
            for contact in self.contacts:
                print(f"👤 Name:  {contact['name']}")
                print(f"📞 Phone: {contact['phone']}")
                print("-" * 30)

    def search_contact(self, name):
        """Search for a contact by name."""
        for contact in self.contacts:
            if contact["name"] == name:
                print(f"   Found!")
                print(f"   Name:  {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                return
        print(f" '{name}' not found in contacts.")


# --- Test ---
if __name__ == "__main__":
    book = ContactBook()
    book.add_contact("Ali", "0300-1234567")
    book.add_contact("Ahmed", "0301-7654321")
    book.add_contact("Sara", "0312-9876543")
    book.add_contact("Kinza", "0333-1111111")
    print()
    book.show_contacts()
    book.search_contact("Ali")
    book.search_contact("Sara")
    book.search_contact("Usman")