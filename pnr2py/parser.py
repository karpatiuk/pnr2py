from .lexer import *
from .struct.PnrData import *
import re


class Parser:
    """
    A class for parsing input text.

    This class is used to parse input text and extract relevant information.
    """

    def __init__(self, input_text):
        """
        Initialize a new Parser instance.

        Args:
            input_text (str): The input text to be parsed.
        """
        self.input_text = input_text

    def parse(self):
        """
        Parse the input text.

        This method should be implemented to parse the input text and extract relevant information.
        """
        lines = self.input_text.split('\n')
        lines = self.__merge_non_new_lines(lines)
        lexer = Lexer(lines)
        lexer.run()
        pnr_data = PnrData(lexer.result)
        pnr_data.populate()

        print(pnr_data.to_json(indent=4))

    @staticmethod
    def __merge_non_new_lines(lines: list) -> list:
        """
        Merge non-new lines if they exceed a certain length.

        This method merges non-new lines if they exceed a specified length by adding them to the previous line.

        Args:
            lines (list): A list of lines to be processed.

        Returns:
            list: A list of lines with non-new lines merged.
        """
        for idx, line in enumerate(lines):
            matches = match_pattern(line,r"\s+")
            if matches and matches.group() is not None and len(matches.group()) > 20:
                try:
                    lines[idx - 1] += ' ' + line.strip()
                except IndexError:
                    pass

        return lines
