import os
import unittest

from source import get_env_from_file


class TestGetEnvFromFile(unittest.TestCase):
    def setUp(self):
        with open('.env', "w") as file:
            file.writelines(['''STR1="abc-123"\n\n''', "STR2 = mixer\n\n\n", '''STR3="3246gt8456$%$^%" # hello\n'''])
            file.writelines(['''NUM1=-123\n\n''', "NUM2 = 118\n", '''NUM3=3246\n'''])

        with open('.env.empty', "w") as file:
            file.writelines("")

    def test_var(self):
        self.assertEqual(get_env_from_file(file_path=".env"),
                         {'STR1': 'abc-123', 'STR2': 'mixer', 'STR3': '3246gt8456$%$^%',
                          'NUM1': '-123', 'NUM2': '118', 'NUM3': '3246'})

    def test_empty_file(self):
        self.assertEqual(get_env_from_file(file_path=".env.empty"), {})

    def tearDown(self):
        os.remove(".env")
        os.remove(".env.empty")
