import re
from app.models.contact import Contact

class ValidationError(Exception):
    pass


def phone_number_duplicate_checker(
        phone:str,contacts: list[Contact],
        current_contact: Contact | None = None) -> None:

    normalized_phone_number = normalize_phone_number(phone)
    for contact in contacts:
        if normalize_phone_number(contact.phone) == normalized_phone_number:
            if current_contact is not None and current_contact.id == contact.id : continue
            raise ValidationError(f"phone number [{phone}] already exists.")



def normalize_phone_number(phone:str) -> str:
    return "".join(d for d in phone if d.isdigit())


def validate_contact(first_name: str,last_name: str,email: str,phone: str) -> None:
    validate_name(first_name,"First Name")
    validate_name(last_name,"Last Name")
    validate_email(email)
    validate_phone(phone)

def validate_name(name: str,field_name: str) -> None:
    name = name.strip()
    if not name:
        raise ValidationError(f"{field_name} can not be empty.")
    
    if len(name)<2 :
        raise ValidationError(f"{field_name} is too short.")
    
    if len(name)>50 :
        raise ValidationError(f"{field_name} is too long.")

def validate_email(email: str) -> None:
    email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
    result = re.fullmatch(email_pattern,email)
    if not result : raise ValidationError(f"email address [{email}] is not correct.")


def validate_phone(phone: str) -> None:
    phone = phone.strip()

    if not phone:
        raise ValidationError("Phone number can not be empty.")

    allowed_chars = set("0123456789+ -()")

    for char in phone:
        if char not in allowed_chars:
            raise ValidationError(f"Phone number [{phone}] is not correct.")

    digits_count = sum(1 for char in phone if char.isdigit())

    if digits_count < 7:
        raise ValidationError("Phone number is too short.")

    if digits_count > 15:
        raise ValidationError("Phone number is too long.")