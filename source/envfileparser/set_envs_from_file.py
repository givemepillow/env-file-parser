import os

from .get_envs_from_file import get_envs_from_file


def set_envs_from_file(key: str, *next_keys: str, file_path: str = ".env", override: bool = True) -> None:
    file_vars = get_envs_from_file(file_path=file_path)
    for v in key, *next_keys:
        if override or os.environ.get(v, '__exists__') == '__exists__':
            os.environ[v] = file_vars[v]
