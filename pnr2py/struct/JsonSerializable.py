import json
from dataclasses import dataclass, asdict


@dataclass
class JsonSerializable:
    """
    A mixin class for JSON serialization of data classes.
    """

    def to_json(self) -> str:
        """
        Serialize the data class to a JSON-formatted string.

        Returns:
            str: JSON-formatted string representing the data class.
        """
        metadata = asdict(self)
        filtered_data = self.filter_dictionary(metadata)
        return json.dumps(filtered_data, indent=2)

    def filter_dictionary(self, data: dict) -> dict:
        """
        Recursively filter a dictionary to remove fields with names containing "__".

        Args:
            data (dict): Input dictionary to be filtered.

        Returns:
            dict: Filtered dictionary.
        """
        new_data = {}

        for key, value in data.items():
            if "__" not in key:
                if isinstance(value, dict):
                    new_data[key] = self.filter_dictionary(value)
                elif isinstance(value, list):
                    new_data[key] = [self.filter_dictionary(item) if isinstance(item, dict) else item for item in value]
                else:
                    new_data[key] = value

        return new_data
