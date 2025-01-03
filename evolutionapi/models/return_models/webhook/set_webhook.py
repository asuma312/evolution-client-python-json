from dataclasses import dataclass
from typing import List

@dataclass
class WebhookDetails:
    url: str
    events: List[str]
    enabled: bool

    @staticmethod
    def from_dict(obj: dict) -> 'WebhookDetails':
        return WebhookDetails(
            obj["url"],
            obj["events"],
            obj["enabled"]
        )

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "events": self.events,
            "enabled": self.enabled
        }

@dataclass
class SetWebhook:
    instanceName: str
    webhook: WebhookDetails

    @staticmethod
    def from_dict(obj: dict) -> 'SetWebhook':
        return SetWebhook(
            obj["instanceName"],
            WebhookDetails.from_dict(obj["webhook"])
        )

    def to_dict(self) -> dict:
        return {
            "instanceName": self.instanceName,
            "webhook": self.webhook.to_dict()
        }
