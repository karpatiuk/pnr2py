import json
from dataclasses import dataclass, field, asdict


@dataclass
class JsonSerializable:
    def to_json(self):
        return json.dumps(asdict(self), indent=4)
