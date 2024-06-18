class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id
    
    def update_contact_details(self, new_contact_details):
        self.contact_details = new_contact_details
        print(f"Contact details updated for {self.name}")
    
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact_details}, Membership ID: {self.membership_id}"

class LibrarySystem:
    def __init__(self):
        self.borrowers = {}
    
    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower
        print(f"Added new borrower: {borrower.name}")
    
    def update_borrower(self, membership_id, new_contact_details):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_contact_details(new_contact_details)
        else:
            print(f"Borrower with membership ID {membership_id} not found.")
    
    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(f"Borrower with membership ID {membership_id} removed from the system.")
        else:
            print(f"Borrower with membership ID {membership_id} not found.")


if __name__ == "__main__":
    library_system = LibrarySystem()
    
    # Add new borrowers
    borrower1 = Borrower("Praneetha", "praneetha1818@gmail.com", "MID001")
    borrower2 = Borrower("vinay", "vinaynakka@gmail.com", "MID002")
    borrower3 = Borrower("soumya", "soumyanakka@gmail.com", "MID003")
    borrower4 = Borrower("kavya", "kavyadurgapu@gmail.com", "MID004")
    borrower5 = Borrower("supraja", "suprajainduri@gmail.com", "MID005")

    
    library_system.add_borrower(borrower1)
    library_system.add_borrower(borrower2)
    library_system.add_borrower(borrower3)
    library_system.add_borrower(borrower4)
    library_system.add_borrower(borrower5)
    
    # Update borrower information
    library_system.update_borrower("MID001", "marripellipraneetha@gmail.com")
    library_system.update_borrower("MID002", "winay2000@gmail.com")
    
    # Remove borrower
    library_system.remove_borrower("MID005")
    
    # Print remaining borrowers (for demonstration)
    for member_id, borrower in library_system.borrowers.items():
        print(borrower)



class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id
    
    def update_contact_details(self, new_contact_details):
        self.contact_details = new_contact_details
        print(f"Contact details updated for {self.name}")
    
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact_details}, Membership ID: {self.membership_id}"

class LibrarySystem:
    def __init__(self):
        self.borrowers = {}
    
    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower
        print(f"Added new borrower: {borrower.name}")
    
    def update_borrower(self, membership_id, new_contact_details):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_contact_details(new_contact_details)
        else:
            print(f"Borrower with membership ID {membership_id} not found.")
    
    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(f"Borrower with membership ID {membership_id} removed from the system.")
        else:
            print(f"Borrower with membership ID {membership_id} not found.")
