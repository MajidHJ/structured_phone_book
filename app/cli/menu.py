from app.models.contact import Contact

class PhoneBookCLI:
    
    def __init__(self) -> None:
        self.contacts: list[Contact] = []
        self.is_running: bool = True


    def run(self):
        while self.is_running:
            self.show_menu()
            choice = input("Choose an option: ").strip()
            self.handle_choice(choice)



    def show_menu(self):
        print("=== PhoneBokk ===")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Exit")
        print("="*15)

    def handle_choice(self,choice):
        
        if choice == "1":
            self.add_contact()
        elif choice == "2":
            self.list_contacts()
        elif choice == "3":
            print("Goodbye! ")
            self.is_running = False
        else:
            print("XX Invalid Input XX")

    def add_contact(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone Number: ")

        contact = Contact(
            first_name= first_name,
            last_name= last_name,
            email= email,
            phone= phone,
        )
        self.contacts.append(contact)

    def list_contacts(self):
        if not self.contacts:
            print("No Contact Found!")
        for c in self.contacts:
            print(c)