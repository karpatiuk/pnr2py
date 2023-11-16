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


def to_camel_case(snake_str: str, first_lower: bool = True) -> str:
    """
    Convert a snake_case string to CamelCase.

    Parameters:
    - snake_str (str): The input string in snake_case.
    - first_lower (bool): If True, the first letter of the result will be in lowercase.
                          If False, the first letter will be in uppercase.

    Returns:
    - str: The input string converted to CamelCase.
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
