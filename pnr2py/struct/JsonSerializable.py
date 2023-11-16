import json
from dataclasses import dataclass, asdict


@dataclass
class JsonSerializable:
    """
    A mixin class for JSON serialization of data classes.
    """

    def to_json(self, remove_none: bool = False, indent: None | int | str = None) -> str:
        """
        Serialize the data class to a JSON-formatted string.

        Args:
            remove_none (bool): If True, remove fields with values of None. Default is False.
            indent (None, int, or str): Number of spaces to use for indentation in the formatted JSON.
                Default is None (no indentation).
        Returns:
            str: JSON-formatted string representing the data class.
        """
        metadata = asdict(self)
        filtered_data = self.filter_dictionary(metadata, remove_none)
        return json.dumps(filtered_data, indent=indent)

    def filter_dictionary(self, data: dict, remove_none: bool = False) -> dict:
        """
        Recursively filter a dictionary to remove fields with names containing "__".

        Args:
            data (dict): Input dictionary to be filtered.
            remove_none (bool): If True, remove fields with values of None. Default is False.

        Returns:
            dict: Filtered dictionary.
        """
        filtered_data = {}

        for key, value in data.items():
            if "__" not in key:
                if isinstance(value, dict):
                    filtered_data[key] = self.filter_dictionary(value, remove_none)
                elif isinstance(value, (list, tuple)):
                    filtered_data[key] = [self.filter_dictionary(item, remove_none) if isinstance(item, dict) else item
                                          for item in value]
                else:
                    if (remove_none is True and value is not None) or remove_none is False:
                        filtered_data[key] = value

        return filtered_data
