from ..patterns import constants
from .Flight import Flight


class PnrData:
    def __init__(self, data):
        self.__data = data

    def populate(self):
        for data in self.__data:
            if len(data.matched_values) > 0:
                flight = Flight()
                for value_type, matched_value in data.matched_values.items():
                    match value_type:
                        case constants.N_LINE_NUMBER:

                            pass
                        case _:
                            pass
