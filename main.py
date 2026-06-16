from models.contact import Contact
from repositories.contact_repository import ContactRepository
contact1 = Contact("John Doe", "john.doe@example.com", "123-456-7890")
contact2 = Contact("Jane Smith", "jane.smith@example.com", "098-765-4321")
repo = ContactRepository()
repo.add(contact1)
repo.add(contact2)


for c in repo.get_all():
    print(c)