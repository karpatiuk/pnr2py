from .patterns import constants
from .helpers.text import *

class Token:
    """
    A class representing a token for parsing.

    This class is used to define tokens with a name, a regex pattern, and a required flag.
    """

    def __init__(self, name, regex, required):
        """
        Initialize a new Token instance.

        Args:
            name (str): The name of the token.
            regex (str): The regular expression pattern for matching this token.
            required (bool): Indicates whether this token is required for parsing.
        """
        self.name = name
        self.regex = regex
        self.required = required


class ItineraryLine:
    """
    A class for parsing itinerary lines.

    This class is used to parse text lines and extract tokens based on predefined patterns.
    """

    def __init__(self, text_line=''):
        """
        Initialize a new ItineraryLine instance.

        Args:
            text_line (str): The text line to be parsed.
        """
        self.tokens = []
        self.text_line = text_line
        self.matched_values = {}
        self.is_error = False
        self.error_token = None
        for pattern in constants.ITINERARY_LINE:
            self.tokens.append(Token(pattern[0], pattern[1], pattern[2]))

    def parse(self):

        """
        Parse the text line using predefined tokens and patterns.

        This method should be implemented to extract tokens from the text_line based on the predefined patterns.
        """
        text_line = self.text_line.strip()
        print(text_line)
        for token in self.tokens:
            # print(text_line)
            matched_value = match_pattern(text_line, token.regex)
            if matched_value is not None:
                self.matched_values[token.name] = matched_value.group()
                text_line = ' ' + text_line[matched_value.end():].strip()+' '
            elif token.required:
                self.is_error = True
                self.error_token = token.name
                break



