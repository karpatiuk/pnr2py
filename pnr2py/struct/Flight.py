from dataclasses import dataclass, field
from .JsonSerializable import JsonSerializable
from .Airport import Airport


@dataclass
class Flight(JsonSerializable):
    departure: Airport = field(default=None)
    arrival: Airport = field(default=None)

    def populate(self, dep_arr):
        pass
