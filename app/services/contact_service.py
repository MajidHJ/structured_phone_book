from app.models.contact import Contact
from app.validators.contact_validator import (
    validate_contact,
    phone_number_duplicate_checker
)
from app.repositories.base_repository import ContactRepository
from datetime import datetime,timezone

class ContactService:
    def __init__(self,repository: ContactRepository) -> None:
        self.repo = repository


    def add_contact(
            self,
            first_name: str,
            last_name: str,
            email: str,
            phone: str,
            ) -> Contact:


        validate_contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
        )

        phone_number_duplicate_checker(phone,self.repo.get_all())

        contact = Contact(
            first_name= first_name,
            last_name= last_name,
            email= email,
            phone= phone,
        )

        self.repo.add(contact)

        return contact
        

    def get_all_contacts(self) -> list[Contact]:
        return self.repo.get_all()

    def get_contact_by_id(self, contact_id: str) -> Contact:
        contact = self.repo.get_by_id(contact_id=contact_id)
        if contact is None :
            raise ValueError("Contact Not Found")
        return contact

    def search(self,query: str) -> list[Contact]:
        query = query.strip().lower()
        if not query: 
            raise ValueError("Search query cannot be empty.")
        
        result = []
        for c in self.repo.get_all():
            if (
                query in c.first_name.lower() or 
                query in c.last_name.lower() or 
                query in c.email.lower() or 
                query in c.phone
            ):
                result.append(c)
        return result

    def delete(self,contact_id: str) -> None:
        deleted_contact = self.repo.delete(contact_id=contact_id)
        if deleted_contact is None:
            raise ValueError("Contact Not Found")


    
    def update(
            self,
            new_first_name: str,
            new_last_name: str,
            new_email: str,
            new_phone: str,
            contact_id: str
            ) -> None:
        
        contact = self.repo.get_by_id(contact_id)
        if contact is None:
            raise ValueError("Contact Not Found")
        
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
            raise ValueError("No Changes Made.")
        
        validate_contact(
            first_name=updated_first_name,
            last_name=updated_last_name,
            email=updated_email,
            phone=updated_phone,
        )      
        phone_number_duplicate_checker(updated_phone,self.repo.get_all(),contact)
        new_contact = Contact(
            id=contact.id,
            first_name=updated_first_name,
            last_name=updated_last_name,
            email=updated_email,
            phone=updated_phone,
            created_at=contact.created_at,
            updated_at=datetime.now(timezone.utc)
        )

        updated_contact = self.repo.update(new_contact)
        if updated_contact is None:
            raise ValueError("Contact Not Found")
           