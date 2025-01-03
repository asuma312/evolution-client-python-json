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
class LocationMessage:
    degreesLatitude: float
    degreesLongitude: float
    name: str
    address: str
    contextInfo: Optional[Dict]  # Pode ser vazio ou um dicionário

    @staticmethod
    def from_dict(obj: dict) -> 'LocationMessage':
        return LocationMessage(
            obj["degreesLatitude"],
            obj["degreesLongitude"],
            obj["name"],
            obj["address"],
            obj.get("contextInfo", {})  # Default para dicionário vazio
        )

    def to_dict(self) -> dict:
        return {
            "degreesLatitude": self.degreesLatitude,
            "degreesLongitude": self.degreesLongitude,
            "name": self.name,
            "address": self.address,
            "contextInfo": self.contextInfo
        }

@dataclass
class MessageDetails:
    locationMessage: LocationMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            LocationMessage.from_dict(obj["locationMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "locationMessage": self.locationMessage.to_dict()
        }

@dataclass
class SendLocation:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendLocation':
        return SendLocation(
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
