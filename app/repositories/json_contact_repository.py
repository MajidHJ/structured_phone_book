from app.models.contact import Contact
from app.repositories.base_repository import ContactRepository
from pathlib import Path
import json
class JsonContactRepository(ContactRepository):

    def __init__(self,file_path = "data/contacts.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True,exist_ok=True)
        self._contacts : list[Contact] = self._load_contacts()


    def add(self, contact: Contact) -> None:
        contacts_backup = self._contacts.copy()
        contacts_backup.append(contact)
        self._save_contacts(contacts_backup)
        self._contacts = contacts_backup

            
    def get_all(self) -> list[Contact]:
        return self._contacts.copy()

    def get_by_id(self, contact_id: str) -> Contact | None:
        for contact in self._contacts:
            if contact.id == contact_id:
                return contact
        return None

    def delete(self, contact_id: str) -> Contact | None:
        contact = self.get_by_id(contact_id)
        if contact is None:
            return None
        contacts_backup = self._contacts.copy()
        contacts_backup.remove(contact)
        self._save_contacts(contacts_backup)
        self._contacts = contacts_backup
        return contact


    def update(self, contact: Contact) -> Contact | None:
        for index,existing_contact in enumerate(self._contacts):
            if existing_contact.id == contact.id:
                new_contacts = self._contacts.copy()
                new_contacts[index] = contact
                self._save_contacts(new_contacts)
                self._contacts = new_contacts
                return contact
        return None
    
    def _save_contacts(self,new_contacts: list[Contact]) -> None:
        contacts = []
        for c in new_contacts:
            contacts.append(c.to_dict())

        try:
            with open(self.file_path,"w",encoding="utf-8") as f:
                json.dump(contacts,f,ensure_ascii=False,indent=2)
        except OSError as error:
            raise ValueError("Saving File Failed.") from error


    def _load_contacts(self) -> list[Contact] :
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                
                contacts = []
                for c in data:
                    contacts.append(Contact.from_dict(c))
                return contacts
            
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except OSError as e:
            raise ValueError("Load File Failed.") from e


