from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Group:
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

    @staticmethod
    def from_dict(obj: dict) -> 'Group':
        return Group(
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
            obj["announce"]
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
            "announce": self.announce
        }

@dataclass
class FetchAllGroups:
    groups: List[Group]

    @staticmethod
    def from_dict(obj: List[dict]) -> 'FetchAllGroups':
        return FetchAllGroups(
            [Group.from_dict(group) for group in obj]
        )

    def to_dict(self) -> List[dict]:
        return [group.to_dict() for group in self.groups]
