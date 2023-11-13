import json
from dataclasses import dataclass, asdict


@dataclass
class JsonSerializable:
    """A mixin class for JSON serialization of data classes."""

    def to_json(self) -> str:
        """
        Serialize the data class to a JSON-formatted string.

        Returns:
            str: JSON-formatted string representing the data class.
        """
        return json.dumps(asdict(self), indent=4)
