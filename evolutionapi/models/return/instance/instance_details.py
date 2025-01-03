from dataclasses import dataclass

@dataclass
class InstanceDetails:
    instanceName: str
    state: str

    @staticmethod
    def from_dict(obj: dict) -> 'InstanceDetails':
        return InstanceDetails(
            obj["instanceName"],
            obj["state"]
        )

    def to_dict(self) -> dict:
        return {
            "instanceName": self.instanceName,
            "state": self.state
        }

@dataclass
class ConnectionState:
    instance: InstanceDetails

    @staticmethod
    def from_dict(obj: dict) -> 'ConnectionState':
        return ConnectionState(
            InstanceDetails.from_dict(obj["instance"])
        )

    def to_dict(self) -> dict:
        return {
            "instance": self.instance.to_dict()
        }
