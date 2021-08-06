import os

from .get_envs_from_file import get_envs_from_file


def set_envs_from_file(key: str, *next_keys: str, file_path=".env"):
    file_vars = get_envs_from_file(file_path=file_path)
    for v in key, *next_keys:
        os.environ[v] = file_vars[v]
