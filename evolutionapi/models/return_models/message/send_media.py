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
class ImageMessage:
    url: str
    mimetype: str
    caption: str
    fileSha256: str
    fileLength: str
    height: int
    width: int
    mediaKey: str
    fileEncSha256: str
    directPath: str
    mediaKeyTimestamp: str
    jpegThumbnail: str
    contextInfo: Optional[Dict]  # Pode ser vazio ou um dicionário

    @staticmethod
    def from_dict(obj: dict) -> 'ImageMessage':
        return ImageMessage(
            obj["url"],
            obj["mimetype"],
            obj["caption"],
            obj["fileSha256"],
            obj["fileLength"],
            obj["height"],
            obj["width"],
            obj["mediaKey"],
            obj["fileEncSha256"],
            obj["directPath"],
            obj["mediaKeyTimestamp"],
            obj["jpegThumbnail"],
            obj.get("contextInfo", {})  # Default para dicionário vazio
        )

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "mimetype": self.mimetype,
            "caption": self.caption,
            "fileSha256": self.fileSha256,
            "fileLength": self.fileLength,
            "height": self.height,
            "width": self.width,
            "mediaKey": self.mediaKey,
            "fileEncSha256": self.fileEncSha256,
            "directPath": self.directPath,
            "mediaKeyTimestamp": self.mediaKeyTimestamp,
            "jpegThumbnail": self.jpegThumbnail,
            "contextInfo": self.contextInfo
        }

@dataclass
class MessageDetails:
    imageMessage: ImageMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            ImageMessage.from_dict(obj["imageMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "imageMessage": self.imageMessage.to_dict()
        }

@dataclass
class SendMedia:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendMedia':
        return SendMedia(
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
