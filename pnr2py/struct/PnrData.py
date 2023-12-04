from dataclasses import dataclass, field
from .JsonSerializable import JsonSerializable
from .Flight import Flight
from typing import List


@dataclass
class PnrData(JsonSerializable):
    __data: dict
    flights: List[Flight] = field(default_factory=list)

    def populate(self):
        for data in self.__data:
            if len(data.matched_values) > 0:
                flight = Flight()
                flight.populate_flight(data.matched_values)
                self.add_flight(flight)

    def add_flight(self, flight: Flight):
        self.flights.append(flight)
