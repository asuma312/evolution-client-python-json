from dataclasses import dataclass
from typing import List

@dataclass
class Participant:
    id: str
    admin: str

    @staticmethod
    def from_dict(obj: dict) -> 'Participant':
        return Participant(
            obj["id"],
            obj["admin"]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "admin": self.admin
        }

@dataclass
class FindGroupMembers:
    participants: List[Participant]

    @staticmethod
    def from_dict(obj: dict) -> 'FindGroupMembers':
        return FindGroupMembers(
            [Participant.from_dict(p) for p in obj["participants"]]
        )

    def to_dict(self) -> dict:
        return {
            "participants": [p.to_dict() for p in self.participants]
        }
