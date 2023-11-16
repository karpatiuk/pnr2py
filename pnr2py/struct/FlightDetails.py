from dataclasses import dataclass, field
from datetime import date, datetime
from .JsonSerializable import JsonSerializable
from ..patterns import constants


def parse_flight_number_text(txt: str) -> dict:
    res = {'booking_class': txt[-1:], 'carrier': txt[:2], 'flight_number': txt[2:-1].strip()}

    return res


@dataclass
class FlightDetails(JsonSerializable):
    __depDate: dict = field(default=None)
    __arrDate: dict = field(default=None)
    __depTime: dict = field(default=None)
    __arrTime: dict = field(default=None)
    flight_number: str = field(default=None)
    carrier_iata_code: str = field(default=None)
    cabin: str = field(default=None)
    booking_class: str = field(default=None)
    departure_date: str = field(default=None)
    arrival_date: str = field(default=None)

    def populate(self, value, value_type: str):
        print(value, value_type)
        match value_type:
            case constants.N_FLIGHT_NUMBER:
                self.populate_flight_number(value)
            case constants.N_DEPARTURE_DATE:
                pass
            case constants.N_DEPARTURE_TIME:
                pass
            case constants.N_ARRIVAL_TIME:
                pass
            case constants.N_ARRIVAL_DATE:
                pass

    def populate_flight_number(self, txt: str):
        res = parse_flight_number_text(txt.strip())
        self.flight_number = res['flight_number']
        self.carrier_iata_code = res['carrier']
        self.booking_class = res['booking_class']

    def parse_date(self, date_string: str, date_type: str):
        month = date_string[-3:]
        day = date_string[:-3]
        match date_type:
            case constants.N_DEPARTURE_DATE:
                self.__depDate['day'] = day
                self.__depDate['month'] = month
            case constants.N_ARRIVAL_DATE:
                self.__arrDate['day'] = day
                self.__arrDate['month'] = month

    def parse_time(self, time_string: str):
        pass
