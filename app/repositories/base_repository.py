from abc import ABC,abstractmethod
from app.models.contact import Contact

class ContactRepository(ABC):
    
    @abstractmethod
    def add(self,contact: Contact) -> None:
        pass


    @abstractmethod
    def get_all(self) -> list[Contact]:
        pass
    

    @abstractmethod
    def get_by_id(self, contact_id: str) -> Contact | None:
        pass


    @abstractmethod
    def delete(self,contact_id:str) -> Contact | None:
        pass


    @abstractmethod
    def update(self, contact: Contact) -> Contact | None:
        pass