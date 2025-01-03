from dataclasses import dataclass

@dataclass
class SettingsDetails:
    rejectCall: bool
    msgCall: str
    groupsIgnore: bool
    alwaysOnline: bool
    readMessages: bool
    syncFullHistory: bool
    readStatus: bool

    @staticmethod
    def from_dict(obj: dict) -> 'SettingsDetails':
        return SettingsDetails(
            obj["rejectCall"],
            obj["msgCall"],
            obj["groupsIgnore"],
            obj["alwaysOnline"],
            obj["readMessages"],
            obj["syncFullHistory"],
            obj["readStatus"]
        )

    def to_dict(self) -> dict:
        return {
            "rejectCall": self.rejectCall,
            "msgCall": self.msgCall,
            "groupsIgnore": self.groupsIgnore,
            "alwaysOnline": self.alwaysOnline,
            "readMessages": self.readMessages,
            "syncFullHistory": self.syncFullHistory,
            "readStatus": self.readStatus
        }

@dataclass
class FindSettings:
    instanceName: str
    settings: SettingsDetails

    @staticmethod
    def from_dict(obj: dict) -> 'FindSettings':
        return FindSettings(
            obj["instanceName"],
            SettingsDetails.from_dict(obj["settings"])
        )

    def to_dict(self) -> dict:
        return {
            "instanceName": self.instanceName,
            "settings": self.settings.to_dict()
        }
