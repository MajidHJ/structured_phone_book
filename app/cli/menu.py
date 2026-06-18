from app.models.contact import Contact
from datetime import datetime
from app.validators.contact_validator import ValidationError,validate_contact, phone_number_duplicate_checker

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
        print("4. Delete")
        print("5. Update")
        print("6. Exit")
        print("="*15)

    def handle_choice(self,choice: str) -> None:
        
        if choice == "1":
            self.add_contact()
        elif choice == "2":
            self.list_contacts()
        elif choice == "3":
            self.search()
        elif choice == "4":
            self.delete()
        elif choice == "5":
            self.update()
        elif choice == "6":
            print("Goodbye! ")
            self.is_running = False
        else:
            print("XX Invalid Input XX")

    def add_contact(self) -> None:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip().lower()
        phone = input("Phone Number: ").strip()

        try:

            validate_contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
            )
        except ValidationError as e:
            print("Error:", e)
            return
        

        try:
            phone_number_duplicate_checker(phone,self.contacts)
        except ValidationError as e:
            print("Error:",e)
            return


        contact = Contact(
            first_name= first_name,
            last_name= last_name,
            email= email,
            phone= phone,
        )
        self.contacts.append(contact)
        print("Contact Added Successfully.")

    def list_contacts(self) -> None:
        if not self.contacts:
            print("No Contact Found.")
            return
        
        for c in self.contacts:
            print(c)
            

    def search(self) -> list[Contact] | None:
        query = input("Enter Something To Search: ").strip().lower()
        if not query: 
            print("Search query cannot be empty.")
            return
        result = []
        for c in self.contacts:
            if (
                query in c.first_name.lower() or 
                query in c.last_name.lower() or 
                query in c.email.lower() or 
                query in c.phone
            ):
                result.append(c)
                print(f"{len(result)}: {c}")

        if not result:
            print("No Contact Found.")
            return None
        
        return result

    def delete(self) -> None:
        result = self.search()
        
        if not result : return

        try:
            idx = int(input("Select Index To Delete: ").strip())
        except ValueError:
            print("Invalid Index.")
            return
        
        if idx > len(result) or idx < 1:
            print("Index Out of Range. ")
            return
        
        contact = result[idx-1]
        confirm = input(f"Are you sure to delete {contact.full_name}? [y/n]:").strip().lower()
        if confirm in ("y","yes"):
            self.contacts.remove(contact)
            print("Contact Removed Successfully.")
        else:
            print("Delete Canceled.")

    
    def update(self) -> None:
        result = self.search()

        if not result:
            return

        try:
            idx = int(input("Select Index To Update: ").strip())
        except ValueError:
            print("Invalid Index.")
            return

        if idx < 1 or idx > len(result):
            print("Index Out of Range.")
            return

        contact = result[idx - 1]

        print("Leave a field empty to keep the current value.")
        print(f"Updating: {contact.full_name}")

        new_first_name = input(f"First Name [{contact.first_name}]: ").strip()
        new_last_name = input(f"Last Name [{contact.last_name}]: ").strip()
        new_email = input(f"Email [{contact.email}]: ").strip().lower()
        new_phone = input(f"Phone [{contact.phone}]: ").strip()

        updated_first_name = new_first_name if new_first_name else contact.first_name
        updated_last_name = new_last_name if new_last_name else contact.last_name
        updated_email = new_email if new_email else contact.email
        updated_phone = new_phone if new_phone else contact.phone

        has_changes = (
            updated_first_name != contact.first_name or
            updated_last_name != contact.last_name or
            updated_email != contact.email or
            updated_phone != contact.phone
        )

        if not has_changes:
            print("No Changes Made.")
            return
        
        try:

            validate_contact(
                first_name=updated_first_name,
                last_name=updated_last_name,
                email=updated_email,
                phone=updated_phone,
            )      
        except ValidationError as e:
            print("Error:", e)
            return 


        try:
            phone_number_duplicate_checker(updated_phone,self.contacts,contact)
        except ValidationError as e:
            print("Error:",e)       
            return

        confirm = input("Save Changes? [y/n]: ").strip().lower()

        if confirm not in ("y", "yes"):
            print("Update Canceled.")
            return

        contact.first_name = updated_first_name
        contact.last_name = updated_last_name
        contact.email = updated_email
        contact.phone = updated_phone
        contact.updated_at = datetime.now()

        print("Contact Updated Successfully.")
        

        


    
                