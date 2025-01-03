from dataclasses import dataclass
from typing import List, Optional

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
class FindGroupByJid:
    id: str
    subject: str
    subjectOwner: str
    subjectTime: int
    pictureUrl: Optional[str]
    size: int
    creation: int
    owner: str
    desc: str
    descId: str
    restrict: bool
    announce: bool
    participants: List[Participant]

    @staticmethod
    def from_dict(obj: dict) -> 'FindGroupByJid':
        return FindGroupByJid(
            obj["id"],
            obj["subject"],
            obj["subjectOwner"],
            obj["subjectTime"],
            obj.get("pictureUrl"),  # Pode ser nulo
            obj["size"],
            obj["creation"],
            obj["owner"],
            obj["desc"],
            obj["descId"],
            obj["restrict"],
            obj["announce"],
            [Participant.from_dict(p) for p in obj["participants"]]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "subject": self.subject,
            "subjectOwner": self.subjectOwner,
            "subjectTime": self.subjectTime,
            "pictureUrl": self.pictureUrl,
            "size": self.size,
            "creation": self.creation,
            "owner": self.owner,
            "desc": self.desc,
            "descId": self.descId,
            "restrict": self.restrict,
            "announce": self.announce,
            "participants": [p.to_dict() for p in self.participants]
        }
