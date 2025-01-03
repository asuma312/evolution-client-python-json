from dataclasses import dataclass
from typing import Optional, Dict

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
class ContactMessage:
    displayName: str
    vcard: str
    contextInfo: Optional[Dict]  # Pode ser vazio ou um dicionário

    @staticmethod
    def from_dict(obj: dict) -> 'ContactMessage':
        return ContactMessage(
            obj["displayName"],
            obj["vcard"],
            obj.get("contextInfo", {})  # Default para dicionário vazio
        )

    def to_dict(self) -> dict:
        return {
            "displayName": self.displayName,
            "vcard": self.vcard,
            "contextInfo": self.contextInfo
        }

@dataclass
class MessageDetails:
    contactMessage: ContactMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            ContactMessage.from_dict(obj["contactMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "contactMessage": self.contactMessage.to_dict()
        }

@dataclass
class SendContact:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendContact':
        return SendContact(
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
