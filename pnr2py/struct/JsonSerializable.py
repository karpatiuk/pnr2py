import json
from dataclasses import dataclass, asdict
from ..helpers.text import to_camel_case


@dataclass
class JsonSerializable:
    """
    A mixin class for JSON serialization of data classes.
    """

    def to_json(self, remove_none: bool = False, camel_case: bool = False, indent: None | int | str = None) -> str:
        """
        Serialize the data class to a JSON-formatted string.

        :param remove_none: If True, remove fields with values of None. Default is False.
        :type remove_none: bool
        :param camel_case: If True, all attributes will be camelCased. Default is False.
        :type camel_case: bool
        :param indent: Number of spaces to use for indentation in the formatted JSON.
                       Default is None (no indentation).
        :type indent: None, int, or str
        :return: JSON-formatted string representing the data class.
        :rtype: str
        """
        metadata = asdict(self)
        filtered_data = self.filter_dictionary(metadata, camel_case, remove_none)
        return json.dumps(filtered_data, indent=indent)

    def filter_dictionary(self, data: dict, camel_case: bool = False, remove_none: bool = False) -> dict:
        """
        Recursively filter a dictionary to remove fields with names containing "__".

        :param data: Input dictionary to be filtered.
        :type data: dict
        :param camel_case: If True, all attributes will be camelCased. Default is False.
        :type camel_case: bool
        :param remove_none: If True, remove fields with values of None. Default is False.
        :type remove_none: bool
        :return: Filtered dictionary.
        :rtype: dict
        """
        filtered_data = {}

        for key, value in data.items():
            if "__" not in key:
                if camel_case:
                    key = to_camel_case(key)
                if isinstance(value, dict):
                    filtered_data[key] = self.filter_dictionary(value, camel_case, remove_none)
                elif isinstance(value, (list, tuple)):
                    filtered_data[key] = [
                        self.filter_dictionary(item, camel_case, remove_none) if isinstance(item, dict) else item
                        for item in value]
                else:
                    if (remove_none is True and value is not None) or remove_none is False:
                        filtered_data[key] = value

        return filtered_data
