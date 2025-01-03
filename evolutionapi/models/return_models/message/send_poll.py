from dataclasses import dataclass
from typing import List, Dict, Optional

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
class PollOption:
    optionName: str

    @staticmethod
    def from_dict(obj: dict) -> 'PollOption':
        return PollOption(
            obj["optionName"]
        )

    def to_dict(self) -> dict:
        return {
            "optionName": self.optionName
        }

@dataclass
class PollCreationMessage:
    name: str
    options: List[PollOption]
    selectableOptionsCount: int

    @staticmethod
    def from_dict(obj: dict) -> 'PollCreationMessage':
        return PollCreationMessage(
            obj["name"],
            [PollOption.from_dict(option) for option in obj["options"]],
            obj["selectableOptionsCount"]
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "options": [option.to_dict() for option in self.options],
            "selectableOptionsCount": self.selectableOptionsCount
        }

@dataclass
class MessageContextInfo:
    messageSecret: str

    @staticmethod
    def from_dict(obj: dict) -> 'MessageContextInfo':
        return MessageContextInfo(
            obj["messageSecret"]
        )

    def to_dict(self) -> dict:
        return {
            "messageSecret": self.messageSecret
        }

@dataclass
class MessageDetails:
    messageContextInfo: Optional[MessageContextInfo]
    pollCreationMessage: PollCreationMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            MessageContextInfo.from_dict(obj["messageContextInfo"]),
            PollCreationMessage.from_dict(obj["pollCreationMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "messageContextInfo": self.messageContextInfo.to_dict(),
            "pollCreationMessage": self.pollCreationMessage.to_dict()
        }

@dataclass
class SendPoll:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendPoll':
        return SendPoll(
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
