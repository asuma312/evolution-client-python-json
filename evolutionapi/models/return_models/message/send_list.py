from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class KeyDetails:
    remoteJid: str
    fromMe: bool
    id: str

    @staticmethod
    def from_dict(obj: dict) -> 'KeyDetails':
        return KeyDetails(
            obj["remoteJid"],
            obj["fromMe"],
            obj["id"]
        )

    def to_dict(self) -> dict:
        return {
            "remoteJid": self.remoteJid,
            "fromMe": self.fromMe,
            "id": self.id
        }

@dataclass
class Row:
    title: str
    description: str
    rowId: str

    @staticmethod
    def from_dict(obj: dict) -> 'Row':
        return Row(
            obj["title"],
            obj["description"],
            obj["rowId"]
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "rowId": self.rowId
        }

@dataclass
class Section:
    title: str
    rows: List[Row]

    @staticmethod
    def from_dict(obj: dict) -> 'Section':
        return Section(
            obj["title"],
            [Row.from_dict(row) for row in obj["rows"]]
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "rows": [row.to_dict() for row in self.rows]
        }

@dataclass
class ListMessage:
    title: str
    description: str
    buttonText: str
    listType: str
    sections: List[Section]
    contextInfo: Optional[Dict]  # Pode ser vazio ou um dicionário

    @staticmethod
    def from_dict(obj: dict) -> 'ListMessage':
        return ListMessage(
            obj["title"],
            obj["description"],
            obj["buttonText"],
            obj["listType"],
            [Section.from_dict(section) for section in obj["sections"]],
            obj.get("contextInfo", {})  # Default para dicionário vazio
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "buttonText": self.buttonText,
            "listType": self.listType,
            "sections": [section.to_dict() for section in self.sections],
            "contextInfo": self.contextInfo
        }

@dataclass
class MessageDetails:
    listMessage: ListMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            ListMessage.from_dict(obj["listMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "listMessage": self.listMessage.to_dict()
        }

@dataclass
class SendList:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendList':
        return SendList(
            KeyDetails.from_dict(obj["key"]),
            MessageDetails.from_dict(obj["message"]),
            obj["messageTimestamp"],
            obj["status"]
        )

    def to_dict(self) -> dict:
        return {
            "key": self.key.to_dict(),
            "message": self.message.to_dict(),
            "messageTimestamp": self.messageTimestamp,
            "status": self.status
        }
