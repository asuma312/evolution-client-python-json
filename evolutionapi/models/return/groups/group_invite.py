from dataclasses import dataclass

@dataclass
class SendGroupInvite:
    send: bool
    inviteUrl: str

    @staticmethod
    def from_dict(obj: dict) -> 'SendGroupInvite':
        return SendGroupInvite(
            obj["send"],
            obj["inviteUrl"]
        )

    def to_dict(self) -> dict:
        return {
            "send": self.send,
            "inviteUrl": self.inviteUrl
        }
