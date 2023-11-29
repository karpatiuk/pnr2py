from dataclasses import dataclass, field
from datetime import datetime
from .JsonSerializable import JsonSerializable
from ..patterns import constants
from ..helpers.text import match_pattern


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
        """
        Parse the time string and store the parsed values in the corresponding class attribute.

        :param time_string: The input time string.
        :type time_string: str
        :param time_type: The type of time, either constants.N_DEPARTURE_TIME or constants.N_ARRIVAL_TIME.
        :type time_type: str
        """
        time_vals = {}
        if time_string[0] in {'#', '*', '-'}:
            modifier = time_string[0]
            time_string = time_string[1:]
            match modifier:
                case '#':
                    time_vals['day_plus'] = 1
                case '*':
                    time_vals['day_plus'] = 2
                case '-':
                    time_vals['day_minus'] = 1

        if 'A' in time_string:
            time_vals['am_pm'] = 'AM'

        if 'P' in time_string:
            time_vals['am_pm'] = 'PM'

        if '+' in time_string or '|' in time_string:
            time_vals['next_day'] = True

        # Extract hour and minutes.
        matched_value = match_pattern(time_string, constants.PATTERN_TIME_STRING)
        if matched_value is not None:
            _dt_string = matched_value.group()
            time_vals['min'] = _dt_string[-2:]
            time_vals['hour'] = _dt_string[:-2].zfill(2)

        # Extract day_plus
        matched_value = match_pattern(time_string, constants.PATTERN_DAY_PLUS_STRING)
        if matched_value is not None:
            _dt_string = matched_value.group()
            time_vals['day_plus'] = int(_dt_string.replace('+', '').replace('#', '').strip())

        # Extract day_minus
        matched_value = match_pattern(time_string, constants.PATTERN_DAY_MINUS)
        if matched_value is not None:
            _dt_string = matched_value.group()
            time_vals['day_minus'] = int(_dt_string.replace('-', '').strip())

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
        """
        Populate the departure date and time based on the stored values.

        This method uses the current date and time and updates the departure date based on the stored day, month,
        and year information in the `__depDate` attribute.

        Prints the hour from the departure date.

        :return: None
        """
        cur_date_time = datetime.now()

        if self.__depDate is not None:

            # Create a departure date object using the stored day, month, and the current year.
            dep_date = datetime.strptime(
                self.__depDate['day'] + self.__depDate['month'].title() + cur_date_time.strftime('%Y'),
                constants.CURR_DATE_GDS_FORMAT)

            print(self.__arrDate)
