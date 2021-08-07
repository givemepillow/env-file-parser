__all__ = ['parse_env', 'line_parser']


def parse_env(env_file_lines: list) -> dict:
    """A function that extracts a variable from a list of strings.

    Each line from the list is parsed bi line_parser()
    Empty lines, lines starting with " # " and
    lines without '=' are skipped. Then all founded key and values
    returned as a dict. If nothing is found -
    will be returned empty dict.

    :param env_file_lines: list of lines
    :type env_file_lines: list
    :return: dict var name - var value
    """
    env_vars = {}
    for line in env_file_lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#' or '=' not in line:
            continue
        key, value = line_parser(line)
        env_vars[key] = value

    return env_vars


def line_parser(line: str) -> tuple[str, str]:
    """ Parse one line.

    Line is divided by the first equal sign.
    The left part is taken for the variable name,
    and the right part is taken for the value.
    Comments to the right of the code are deleted.
    The value will always be stored as a string.

    :param line: line with key and value
    :type line: str
    :return: tuple(key, value) as strings
    """
    equal_index = line.index('=')
    value = line[equal_index + 1::].strip()

    if '#' in value:
        # If values start from quote.
        if value[0] in ("'", '"'):
            # Finding the index of the closing quotation mark.
            last_quote_index = value.index(value[0])
            for i, c in enumerate(value):
                if c == value[0] and i > last_quote_index:
                    last_quote_index = i
                    break
            # Search for the first '#' character after the closing quotation mark.
            sharp_index = value.index('#')
            for i, c in enumerate(value):
                if c == '#' and i > last_quote_index:
                    sharp_index = i
                    break
            # Deleting a comment if the ' # ' character is placed after the closing quotation marks.
            if last_quote_index < sharp_index:
                value = value[0:sharp_index].strip()
        # If there were no quotes.
        else:
            value = value[0:value.index('#')].strip()

    # Removing quotes, but only if there is an opening and closing one.
    if value[0] in ('"', "'") and value[0] == value[-1]:
        value = value.removeprefix(value[0]).removesuffix(value[-1])

    return line[0:equal_index].strip(), value.strip()
