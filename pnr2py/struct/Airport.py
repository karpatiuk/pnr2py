from dataclasses import dataclass, field
from .JsonSerializable import JsonSerializable


@dataclass
class Airport(JsonSerializable):
    name: str = field(default=None)
    iata: str = field(default=None)
    icao: str = field(default=None)

    def populate(self, iata):
        pass
