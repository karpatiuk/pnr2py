import re


def match_pattern(text: str, pattern: str) -> re.Match or None:
    """
    Search for a pattern in the given text and return the first match.

    :param text: The text in which to search for the pattern.
    :type text: str
    :param pattern: The regular expression pattern to search for.
    :type pattern: str

    :return: If a match is found, it returns the re.Match object.
             Otherwise, it returns None.
    :rtype: re.Match or None
    """
    matches = re.search(pattern, text)
    return matches


def to_camel_case(snake_str: str, first_lower: bool = True) -> str:
    """
    Convert a snake_case string to CamelCase.

    :param snake_str: The input string in snake_case.
    :type snake_str: str
    :param first_lower: If True, the first letter of the result will be in lowercase.
                        If False, the first letter will be in uppercase.
    :type first_lower: bool

    :return: The input string converted to CamelCase.
    :rtype: str
    """
    # Split the snake_case string into a list of words using "_" as the delimiter.
    words = snake_str.lower().split("_")

    # Capitalize each word and join them to form the CamelCase string.
    camel_cased_text = "".join(word.capitalize() for word in words)

    # Adjust the first letter based on the 'first_lower' parameter.
    if first_lower:
        camel_cased_text = camel_cased_text[0].lower() + camel_cased_text[1:]

    # Return the final CamelCase string.
    return camel_cased_text
