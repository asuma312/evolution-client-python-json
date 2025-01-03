from dataclasses import dataclass

@dataclass
class InstanceConnect:
    pairingCode: str
    code: str
    count: int

    @staticmethod
    def from_dict(obj: dict) -> 'InstanceConnect':
        return InstanceConnect(
            obj["pairingCode"],
            obj["code"],
            obj["count"]
        )

    def to_dict(self) -> dict:
        return {
            "pairingCode": self.pairingCode,
            "code": self.code,
            "count": self.count
        }
