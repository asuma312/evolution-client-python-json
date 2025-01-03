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
    backgroundArgb: int
    font: str

    @staticmethod
    def from_dict(obj: dict) -> 'ExtendedTextMessage':
        return ExtendedTextMessage(
            obj["text"],
            obj["backgroundArgb"],
            obj["font"]
        )

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "backgroundArgb": self.backgroundArgb,
            "font": self.font
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
class SendStatus:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str
    participant: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendStatus':
        return SendStatus(
            KeyDetails.from_dict(obj["key"]),
            MessageDetails.from_dict(obj["message"]),
            obj["messageTimestamp"],
            obj["status"],
            obj["participant"]
        )

    def to_dict(self) -> dict:
        return {
            "key": self.key.to_dict(),
            "message": self.message.to_dict(),
            "messageTimestamp": self.messageTimestamp,
            "status": self.status,
            "participant": self.participant
        }
