from dataclasses import dataclass

@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: str

    def __str__(self):
        return f"Contact(first_name={self.first_name}, last_name={self.last_name}, email={self.email}, phone={self.phone})"
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"