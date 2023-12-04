from dataclasses import dataclass, field
from .JsonSerializable import JsonSerializable


@dataclass
class Airport(JsonSerializable):
    name: str = field(default=None)
    iata: str = field(default=None)
    icao: str = field(default=None)
    lat: str = field(default=None)
    long: str = field(default=None)

    def populate(self, iata: str | None = None, name: str | None = None, icao: str | None = None):
        self.name = name
        self.iata = iata
        self.icao = icao
