from dataclasses import dataclass

@dataclass
class FetchInstanceIntegration:
    integration: str
    webhook_wa_business: str

    @staticmethod
    def from_dict(obj: dict) -> 'FetchInstanceIntegration':
        return FetchInstanceIntegration(
            obj["integration"],
            obj["webhook_wa_business"]
        )

    def to_dict(self) -> dict:
        return {
            "integration": self.integration,
            "webhook_wa_business": self.webhook_wa_business
        }
@dataclass
class FetchInstance:
    instanceName: str
    instanceId: str
    owner: str
    profileName: str
    profilePictureUrl: str
    profileStatus: str
    status: str
    serverUrl: str
    apikey: str
    integration: FetchInstanceIntegration

    @staticmethod
    def from_dict(obj: dict) -> 'FetchInstance':
        return FetchInstance(
            obj["instanceName"],
            obj["instanceId"],
            obj["owner"],
            obj["profileName"],
            obj["profilePictureUrl"],
            obj["profileStatus"],
            obj["status"],
            obj["serverUrl"],
            obj["apikey"],
            FetchInstanceIntegration.from_dict(obj["integration"])
        )

    def to_dict(self) -> dict:
        return {
            "instanceName": self.instanceName,
            "instanceId": self.instanceId,
            "owner": self.owner,
            "profileName": self.profileName,
            "profilePictureUrl": self.profilePictureUrl,
            "profileStatus": self.profileStatus,
            "status": self.status,
            "serverUrl": self.serverUrl,
            "apikey": self.apikey,
            "integration": self.integration.to_dict()
        }