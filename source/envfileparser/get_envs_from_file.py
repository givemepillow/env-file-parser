from .base.parser import parser
from .base.reader import read_env


def get_envs_from_file(file_path: str = ".env") -> dict:
    """Unifying function.

    This function allows you to return dict with all values in file.
    The values are represented as strings.

    :param file_path: the string is the path to the file, it has a default value
    :return:
        for zero var names - dict of all variables in file,
        if there no variables - empty dict
    """
    env_file_lines = read_env(file_path)
    env_vars = parser(env_file_lines)
    return env_vars
