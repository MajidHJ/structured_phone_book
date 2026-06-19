from app.models.contact import Contact
from app.repositories.base_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):
    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    def add(self, contact: Contact) -> None:
        self._contacts.append(contact)

    
    def get_all(self) -> list[Contact]:
        return self._contacts.copy()
    

    def get_by_id(self, contact_id: str) -> Contact | None:
        for contact in self._contacts:
            if contact.id == contact_id:
                return contact
        return None
    
    def delete(self, contact_id:str) -> Contact | None:
        contact = self.get_by_id(contact_id)
        if contact is None:
            return None
        
        self._contacts.remove(contact)
        return contact


    def update(self, contact: Contact) -> Contact | None:
        for index,existing_contact in enumerate(self._contacts):
            if existing_contact.id == contact.id:
                self._contacts[index] = contact
                return contact
        return None