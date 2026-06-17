from app.models.contact import Contact

class PhoneBookCLI:
    
    def __init__(self) -> None:
        self.contacts: list[Contact] = []
        self.is_running: bool = True


    def run(self) -> None:
        while self.is_running:
            self.show_menu()
            choice = input("Choose an option: ").strip()
            self.handle_choice(choice)



    def show_menu(self) -> None:
        print("=== PhoneBook ===")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Search")
        print("4. Exit")
        print("="*15)

    def handle_choice(self,choice: str) -> None:
        
        if choice == "1":
            self.add_contact()
        elif choice == "2":
            self.list_contacts()
        elif choice == "3":
            self.search()
        elif choice == "4":
            print("Goodbye! ")
            self.is_running = False
        else:
            print("XX Invalid Input XX")

    def add_contact(self) -> None:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip().lower()
        phone = input("Phone Number: ").strip()

        contact = Contact(
            first_name= first_name,
            last_name= last_name,
            email= email,
            phone= phone,
        )
        self.contacts.append(contact)

    def list_contacts(self) -> None:
        if not self.contacts:
            print("No Contact Found.")
        for c in self.contacts:
            print(c)
            

    def search(self) -> None:
        query = input("Enter Something To Search: ").strip().lower()
        if not query: 
            print("Search query cannot be empty.")
            return
        found = False
        
        for c in self.contacts:
            if (
                query in c.first_name.lower() or 
                query in c.last_name.lower() or 
                query in c.email.lower() or 
                query in c.phone
            ):
                found = True
                print(c)

        if not found:
            print("No Contact Found.")

    
                