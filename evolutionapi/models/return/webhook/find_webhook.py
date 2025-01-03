from dataclasses import dataclass
from typing import List

@dataclass
class FindWebhook:
    enabled: bool
    url: str
    events: List[str]

    @staticmethod
    def from_dict(obj: dict) -> 'FindWebhook':
        return FindWebhook(
            obj["enabled"],
            obj["url"],
            obj["events"]
        )

    def to_dict(self) -> dict:
        return {
            "enabled": self.enabled,
            "url": self.url,
            "events": self.events
        }
