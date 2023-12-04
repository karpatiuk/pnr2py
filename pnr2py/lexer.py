from .token import *


class Lexer:
    """
    A class for lexical analysis.

    This class is responsible for performing lexical analysis on a list of input lines.
    It breaks down the input into tokens for further processing.
    """
    ITINERARY = 'ITINERARY'

    CONTENT_TYPES = [
        ITINERARY
    ]

    def __init__(self, lines):
        """
        Initialize a new Lexer instance.

        Args:
            lines (list): A list of input lines to perform lexical analysis on.
        """
        self.lines = lines
        self.result = []
        self.error_lines = []

    def run(self):
        """
        Perform lexical analysis on the input lines.

        """

        for line in self.lines:
            itinerary_line = ItineraryLine(line)
            itinerary_line.parse()
            if itinerary_line.is_error:
                self.error_lines.append(line)
                del itinerary_line
            else:
                self.result.append(itinerary_line)

    @property
    def has_errors(self):
        return len(self.error_lines) > 0
