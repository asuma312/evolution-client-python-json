from dataclasses import dataclass

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
class ExtendedTextMessage:
    text: str

    @staticmethod
    def from_dict(obj: dict) -> 'ExtendedTextMessage':
        return ExtendedTextMessage(
            obj["text"]
        )

    def to_dict(self) -> dict:
        return {
            "text": self.text
        }

@dataclass
class MessageDetails:
    extendedTextMessage: ExtendedTextMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            ExtendedTextMessage.from_dict(obj["extendedTextMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "extendedTextMessage": self.extendedTextMessage.to_dict()
        }

@dataclass
class SendMessage:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendMessage':
        return SendMessage(
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
