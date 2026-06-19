from dataclasses import dataclass,field
from uuid import uuid4
from datetime import datetime,timezone

@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: str
    id: str = field(default_factory =lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


    def __str__(self):
        return f"Contact(first_name={self.first_name}, last_name={self.last_name}, email={self.email}, phone={self.phone})"
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def to_dict(self) -> dict[str,str] :
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls,data: dict[str,str]) -> "Contact":
        return cls(
            id= data["id"],
            first_name= data["first_name"],
            last_name= data["last_name"],
            email = data["email"],
            phone = data["phone"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at= datetime.fromisoformat(data["updated_at"]),
        )
