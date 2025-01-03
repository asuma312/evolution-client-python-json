from dataclasses import dataclass
from typing import Dict

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
class ReactionMessage:
    key: KeyDetails
    text: str
    senderTimestampMs: str

    @staticmethod
    def from_dict(obj: dict) -> 'ReactionMessage':
        return ReactionMessage(
            KeyDetails.from_dict(obj["key"]),
            obj["text"],
            obj["senderTimestampMs"]
        )

    def to_dict(self) -> dict:
        return {
            "key": self.key.to_dict(),
            "text": self.text,
            "senderTimestampMs": self.senderTimestampMs
        }

@dataclass
class MessageDetails:
    reactionMessage: ReactionMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            ReactionMessage.from_dict(obj["reactionMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "reactionMessage": self.reactionMessage.to_dict()
        }

@dataclass
class SendReaction:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendReaction':
        return SendReaction(
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
