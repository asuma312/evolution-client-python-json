from dataclasses import dataclass

@dataclass
class CreateInstanceInstance:
    instanceName: str
    instanceId: str
    webhook_wa_business: str
    access_token_wa_business: str
    status: str

    @staticmethod
    def from_dict(obj: dict) -> 'CInstanceInstance':
        return CreateInstanceInstance(
            obj["instanceName"],
            obj["instanceId"],
            obj["webhook_wa_business"],
            obj["access_token_wa_business"],
            obj["status"]
        )

    def to_dict(self) -> dict:
        return {
            "instanceName": self.instanceName,
            "instanceId": self.instanceId,
            "webhook_wa_business": self.webhook_wa_business,
            "access_token_wa_business": self.access_token_wa_business,
            "status": self.status
        }

@dataclass
class CreateInstanceHash:
    apikey: str

    @staticmethod
    def from_dict(obj: dict) -> 'CInstanceHash':
        return CreateInstanceHash(obj["apikey"])

    def to_dict(self) -> dict:
        return {"apikey": self.apikey}

@dataclass
class CreateInstanceSettings:
    reject_call: bool
    msg_call: str
    groups_ignore: bool
    always_online: bool
    read_messages: bool
    read_status: bool
    sync_full_history: bool

    @staticmethod
    def from_dict(obj: dict) -> 'CInstanceSettings':
        return CreateInstanceSettings(
            obj["reject_call"],
            obj["msg_call"],
            obj["groups_ignore"],
            obj["always_online"],
            obj["read_messages"],
            obj["read_status"],
            obj["sync_full_history"]
        )

    def to_dict(self) -> dict:
        return {
            "reject_call": self.reject_call,
            "msg_call": self.msg_call,
            "groups_ignore": self.groups_ignore,
            "always_online": self.always_online,
            "read_messages": self.read_messages,
            "read_status": self.read_status,
            "sync_full_history": self.sync_full_history
        }

@dataclass
class CreateInstance:
    instance: CreateInstanceInstance
    hash: CreateInstanceHash
    settings: CreateInstanceSettings

    @staticmethod
    def from_dict(obj: dict) -> 'CreateInstance':
        return CreateInstance(
            CreateInstanceInstance.from_dict(obj["instance"]),
            CreateInstanceHash.from_dict(obj["hash"]),
            CreateInstanceSettings.from_dict(obj["settings"])
        )

    def to_dict(self) -> dict:
        return {
            "instance": self.instance.to_dict(),
            "hash": self.hash.to_dict(),
            "settings": self.settings.to_dict()
        }