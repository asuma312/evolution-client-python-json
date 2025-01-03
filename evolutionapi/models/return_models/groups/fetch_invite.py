from dataclasses import dataclass

@dataclass
class FetchInviteCode:
    inviteUrl: str
    inviteCode: str

    @staticmethod
    def from_dict(obj: dict) -> 'FetchInviteCode':
        return FetchInviteCode(
            obj["inviteUrl"],
            obj["inviteCode"]
        )

    def to_dict(self) -> dict:
        return {
            "inviteUrl": self.inviteUrl,
            "inviteCode": self.inviteCode
        }
