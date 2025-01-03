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
class AudioMessage:
    url: str
    mimetype: str
    fileSha256: str
    fileLength: str
    seconds: int
    ptt: bool
    mediaKey: str
    fileEncSha256: str
    directPath: str
    mediaKeyTimestamp: str

    @staticmethod
    def from_dict(obj: dict) -> 'AudioMessage':
        return AudioMessage(
            obj["url"],
            obj["mimetype"],
            obj["fileSha256"],
            obj["fileLength"],
            obj["seconds"],
            obj["ptt"],
            obj["mediaKey"],
            obj["fileEncSha256"],
            obj["directPath"],
            obj["mediaKeyTimestamp"]
        )

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "mimetype": self.mimetype,
            "fileSha256": self.fileSha256,
            "fileLength": self.fileLength,
            "seconds": self.seconds,
            "ptt": self.ptt,
            "mediaKey": self.mediaKey,
            "fileEncSha256": self.fileEncSha256,
            "directPath": self.directPath,
            "mediaKeyTimestamp": self.mediaKeyTimestamp
        }

@dataclass
class MessageDetails:
    audioMessage: AudioMessage

    @staticmethod
    def from_dict(obj: dict) -> 'MessageDetails':
        return MessageDetails(
            AudioMessage.from_dict(obj["audioMessage"])
        )

    def to_dict(self) -> dict:
        return {
            "audioMessage": self.audioMessage.to_dict()
        }

@dataclass
class SendAudio:
    key: KeyDetails
    message: MessageDetails
    messageTimestamp: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendAudio':
        return SendAudio(
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
