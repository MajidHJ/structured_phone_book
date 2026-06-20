from app.cli.menu import PhoneBookCLI
from app.services.contact_service import ContactService
from app.repositories.json_contact_repository import JsonContactRepository
def main() -> None:
    j_repo = JsonContactRepository()
    service = ContactService(j_repo)
    cli = PhoneBookCLI(service)
    cli.run()


if __name__ == "__main__":
    main()