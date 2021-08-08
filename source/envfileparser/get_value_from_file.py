from .base.parser import line_parser
from .base.reader import read_env

__all__ = ['get_value_from_file', 'get_env']


def get_value_from_file(key: str, file_path: str =".env") -> str:
    """A function that returns value of the specified variables as a string.

    The var name is passed to the function as a string.
    and a named parameter - the path to the file with a default value.
    String value of found variable is returned - otherwise return empty string.

    :param key: name of extracted variable
    :param file_path: the string is the path to the file, it has a default value
    :return: value of extracted var as a string
    """
    if ' ' in key:
        raise ValueError(f"envfileparser: The key {key} must not contain spaces.")
    value = ''
    env_file_lines = read_env(file_path=file_path)
    for line in env_file_lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#' or '=' not in line:
            continue
        parsed_key, parsed_value = line_parser(line)
        if ' ' in parsed_key:
            continue
        elif parsed_key == key:
            value = parsed_value

    if value == '':
        raise KeyError(f"envfileparser: The key \"{key}\" not found in {file_path}.")

    return value


# Deprecated! Left for compatibility support.
get_env = get_value_from_file
