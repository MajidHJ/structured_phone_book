from models.contact import Contact

class ContactRepository:
    def __init__(self):
        self._contacts = []

    def add(self,contact: Contact) -> None:
        self._contacts.append(contact)

    

    def get_all(self) -> list[Contact]:
        return self._contacts