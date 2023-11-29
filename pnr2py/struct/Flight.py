from dataclasses import dataclass, field
from .JsonSerializable import JsonSerializable
from .Airport import Airport
from ..patterns import constants
from .FlightDetails import FlightDetails


@dataclass
class Flight(JsonSerializable):
    line_number: int = field(default=None)
    departure: Airport = field(default=None)
    arrival: Airport = field(default=None)
    details: FlightDetails = field(default=None)

    def populate_flight(self, flight_vals: dict):
        flt_details: FlightDetails = FlightDetails()
        for value_type, value in flight_vals.items():
            match value_type:
                case constants.N_LINE_NUMBER:
                    self.line_number = int(value.replace('.', '').replace('*', ''))
                case constants.N_AIRPORTS:
                    self.populate_airports(str(value).strip())
                case _:
                    flt_details.populate(str(value).strip(), value_type)
                    # print(value)
                    pass
        self.details = flt_details

    def populate_airports(self, dep_arr: str):
        dep, arr = dep_arr[:3], dep_arr[2:5]
        self.departure = Airport(iata=dep)
        self.arrival = Airport(iata=arr)
