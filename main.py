from app.cli.menu import PhoneBookCLI
from app.services.contact_service import ContactService
from app.repositories.in_memory_contact_repository import InMemoryContactRepository

def main() -> None:
    repo = InMemoryContactRepository()
    service = ContactService(repo)
    cli = PhoneBookCLI(service)
    cli.run()


if __name__ == "__main__":
    main()