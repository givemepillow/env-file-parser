import os

from .get_env_from_file import get_env_from_file


def set_env_from_file(*var_names: str, file_path=".env"):
    file_vars = get_env_from_file(file_path=file_path)
    for v in var_names:
        os.environ[v] = file_vars[v]
