import os

from .get_envs_from_file import get_envs_from_file


def set_envs_from_file(key: str, *next_keys: str, file_path: str = ".env", override: bool = False) -> None:
    """

    :param key: str: one required argument is the variable name
    :param next_keys: str: an optional argument is a sequence of names
    :param file_path: str: the file path
    :param override: bool: flag for overwriting environment variables
    :return:
    """
    file_vars = get_envs_from_file(file_path=file_path)
    for v in key, *next_keys:
        if override or os.environ.get(v, '__not_exists__') == '__not_exists__':
            os.environ[v] = file_vars[v]
        else:
            raise KeyError(f"Key {v} is already exists in environment!")
