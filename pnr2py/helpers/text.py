import re


def match_pattern(text, pattern):
    """
    Search for a pattern in the given text and return the first match.

    Args:
        text (str): The text in which to search for the pattern.
        pattern (str): The regular expression pattern to search for.

    Returns:
        re.Match or None: If a match is found, it returns the re.Match object.
            Otherwise, it returns None.
    """
    matches = re.search(pattern, text)

    return matches
