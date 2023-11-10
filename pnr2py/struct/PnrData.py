from dataclasses import dataclass, field
from ..patterns import constants
from .JsonSerializable import JsonSerializable
from .Flight import Flight


@dataclass
class PnrData(JsonSerializable):
    __data: dict
    flights: list = field(default_factory=list)

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
