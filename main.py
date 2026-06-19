from app.cli.menu import PhoneBookCLI
from app.services.contact_service import ContactService

def main() -> None:
    service = ContactService()
    cli = PhoneBookCLI(service)
    cli.run()


if __name__ == "__main__":
    main()