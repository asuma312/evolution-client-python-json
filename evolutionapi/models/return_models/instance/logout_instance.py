from dataclasses import dataclass

@dataclass
class ResponseDetails:
    message: str

    @staticmethod
    def from_dict(obj: dict) -> 'ResponseDetails':
        return ResponseDetails(
            obj["message"]
        )

    def to_dict(self) -> dict:
        return {
            "message": self.message
        }

@dataclass
class LogoutInstance:
    status: str
    error: bool
    response: ResponseDetails

    @staticmethod
    def from_dict(obj: dict) -> 'LogoutInstance':
        return LogoutInstance(
            obj["status"],
            obj["error"],
            ResponseDetails.from_dict(obj["response"])
        )

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "error": self.error,
            "response": self.response.to_dict()
        }
