from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Task:
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None
    id: str = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.created_at is None:
            self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    @classmethod
    def from_dict(cls, data):
        created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            completed=data["completed"],
            created_at=created_at
        )
