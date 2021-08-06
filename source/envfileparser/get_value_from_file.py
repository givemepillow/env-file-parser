from .parse_env import line_parser
from .read_env import read_env


def get_value_from_file(key: str, file_path=".env") -> str:
    """A function that returns value of the specified variables as a string.
    Wrapper for the old get_env.

    :param key: name of extracted variable
    :param file_path: the string is the path to the file, it has a default value
    :return: value of extracted var as a string
    """
    return get_env(key, file_path=file_path)


def get_env(var_name: str, file_path=".env") -> str:
    """A function that returns value of the specified variables as a string.
    Deprecated! Left for compatibility support.

    The var name is passed to the function as a string.
    and a named parameter - the path to the file with a default value.
    String value of found variable is returned - otherwise return empty string.

    :param var_name: name of extracted variable
    :param file_path: the string is the path to the file, it has a default value
    :return: value of extracted var as a string
    """
    empty_value = ''
    env_file_lines = read_env(file_path=file_path)
    for line in env_file_lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#' or '=' not in line:
            continue
        key, parsed_value = line_parser(line)
        if key == var_name:
            return parsed_value

    return empty_value
