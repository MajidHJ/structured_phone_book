from app.services.contact_service import ContactService
from app.validators.contact_validator import ValidationError

class PhoneBookCLI:
    
    def __init__(self,service: ContactService) -> None:
        self.service = service
        self.is_running: bool = True
        self.search_result_map: dict[int, str] = {}


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
        
        try :

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.show_contacts()
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
        except (ValidationError,ValueError) as exc:
            print("Error:",exc)


    def add_contact(self) -> None:
        
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip().lower()
        phone = input("Phone Number: ").strip()

        self.service.add_contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
            )
        print("Contact Added Successfully.")
        
    def show_contacts(self) -> None:
        contacts = self.service.get_all_contacts()
        if not contacts:
            print("No Contact Found.")
            return
        for c in contacts:
            print(c)
    
    def search(self) -> bool:

        query = input("Enter Something To Search: ").strip().lower()
        result = self.service.search(query=query)
        if not result:
            print("No Contact Found.")
            return False
        self.search_result_map.clear()
        for idx,c in enumerate(result,1):
                print(f"{idx}: {c}")
                self.search_result_map[idx] = c.id
        return True

    def delete(self) -> None:
        if not self.search(): 
            return
        idx = input("Select Index To Delete: ").strip()
        contact_id = self.get_contact_id_from_search_result_by_index(idx)
        contact = self.service.get_contact_by_id(contact_id=contact_id)
        confirm = input(f"Are you sure to delete {contact.full_name}? [y/n]:").strip().lower()
        if confirm in ("y","yes"):
            self.service.delete(contact_id)
            print("Contact Removed Successfully.")
        else:
            print("Delete Canceled.")
    
    def update(self) -> None:
        if not self.search():
            return
        
        idx = input("Select Index To Update: ").strip()
        contact_id = self.get_contact_id_from_search_result_by_index(idx)
        contact = self.service.get_contact_by_id(contact_id=contact_id)
        print("Leave a field empty to keep the current value.")
        print(f"Updating: {contact.full_name}")
        new_first_name = input(f"First Name [{contact.first_name}]: ").strip()
        new_last_name = input(f"Last Name [{contact.last_name}]: ").strip()
        new_email = input(f"Email [{contact.email}]: ").strip().lower()
        new_phone = input(f"Phone [{contact.phone}]: ").strip()

        confirm = input("Save Changes? [y/n]: ").strip().lower()

        if confirm not in ("y", "yes"):
            print("Update Canceled.")
            return

        self.service.update(
            new_first_name=new_first_name,
            new_last_name=new_last_name,
            new_email=new_email,
            new_phone=new_phone,
            contact_id=contact_id
        )
        
        print("Contact Updated Successfully.")

    def get_contact_id_from_search_result_by_index(self,index: str) -> str:
        if not index.isdigit() :
            raise ValueError("Invalid Index.")
        idx = int(index)
        if idx > len(self.search_result_map) or idx < 1:
            raise ValueError("Index Out of Range.")
        return self.search_result_map[idx]       




        



        


    
                