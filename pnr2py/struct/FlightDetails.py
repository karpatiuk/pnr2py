from dataclasses import dataclass, field
from datetime import datetime
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

    def populate(self, value: str, value_type: str):
        print(value, value_type)
        match value_type:
            case constants.N_FLIGHT_NUMBER:
                self.populate_flight_number(value)
            case constants.N_DEPARTURE_DATE:
                self.parse_date(value.strip(), constants.N_DEPARTURE_DATE)
            case constants.N_DEPARTURE_TIME:
                self.parse_time(value.strip(), constants.N_DEPARTURE_TIME)
            case constants.N_ARRIVAL_TIME:
                self.parse_time(value.strip(), constants.N_ARRIVAL_TIME)
            case constants.N_ARRIVAL_DATE:
                self.parse_date(value, constants.N_ARRIVAL_DATE)

        self.populate_date_time()

    def populate_flight_number(self, txt: str):
        res = parse_flight_number_text(txt.strip())
        self.flight_number = res['flight_number']
        self.carrier_iata_code = res['carrier']
        self.booking_class = res['booking_class']

    def parse_date(self, date_string: str, date_type: str):
        """
        Parse the date string and store the day and month in the corresponding class attribute.

        :param date_string: The input date string.
        :type date_string: str
        :param date_type: The type of date, either constants.N_DEPARTURE_DATE or constants.N_ARRIVAL_DATE.
        :type date_type: str
        """
        # Extract the last 3 characters as month and the first 2 characters as day.
        month = date_string[-3:]
        day = date_string[:2]
        date_vals = {'day': day, 'month': month}
        match date_type:
            case constants.N_DEPARTURE_DATE:
                if self.__depDate is None:
                    self.__depDate = date_vals
                else:
                    self.__depDate.update(date_vals)
            case constants.N_ARRIVAL_DATE:
                if self.__arrDate is None:
                    self.__arrDate = date_vals
                else:
                    self.__arrDate.update(date_vals)

    def parse_time(self, time_string: str, time_type: str):
        time_vals = {}
        match time_string[0]:
            case '#':
                time_vals['day_plus'] = 1
                time_string = time_string[1:]
            case '*':
                time_vals['day_plus'] = 2
                time_string = time_string[1:]
            case '-':
                time_vals['day_minus'] = 1
                time_string = time_string[1:]

        if time_string.find('A') != -1:
            time_vals['am_pm'] = 'AM'

        if time_string.find('P') != -1:
            time_vals['am_pm'] = 'PM'

        if time_string.find('+') != -1 or time_string.find('|') != -1:
            time_vals['next_day'] = True

        match time_type:
            case constants.N_DEPARTURE_TIME:
                if self.__depDate is None:
                    self.__depDate = time_vals
                else:
                    self.__depDate.update(time_vals)

            case constants.N_ARRIVAL_TIME:
                if self.__arrDate is None:
                    self.__arrDate = time_vals
                else:
                    self.__arrDate.update(time_vals)

    def populate_date_time(self):
        cur_date_time = datetime.now()
        if self.__depDate is not None:
            # print(self.__depDate.get('month').title())
            dep_date = datetime.strptime(
                self.__depDate['day'] + self.__depDate['month'].title() + cur_date_time.strftime('%Y'),
                constants.CURR_DATE_GDS_FORMAT)
            print(dep_date)
        pass
