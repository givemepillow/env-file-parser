import os
import unittest

from source import load_env_from_file, get_env


class TestGetEnvsFromFile(unittest.TestCase):
    def setUp(self):
        with open('.env', "w") as file:
            file.write(
                "# env vars to set\n"
                "MY_VAR = 'test_var'\n"
                "\n\n"
                "MY_VAR_ONE = '1' # one\n"
                "MY_VAR_TWO = 2 ## two\n"
            )

    def test_set_vars(self):
        load_env_from_file('MY_VAR', 'MY_VAR_ONE', 'MY_VAR_TWO')
        self.assertTrue(get_env('MY_VAR', file_path=".env"), os.environ.get('MY_VAR'))
        self.assertTrue(get_env('MY_VAR', file_path=".env"), os.environ.get('MY_VAR_ONE'))
        self.assertTrue(get_env('MY_VAR', file_path=".env"), os.environ.get('MY_VAR_TWO'))

    def tearDown(self):
        os.environ.pop('MY_VAR_ONE')
        os.environ.pop('MY_VAR_TWO')
        os.environ.pop('MY_VAR')
        os.remove(".env")
