import os
import unittest

from source import get_env_from_file


class TestGetEnvsFromFile(unittest.TestCase):
    def setUp(self):
        with open('.env1', "w") as file:
            file.writelines(['''STR1="abc-123"\n\n''',
                             "STR2 = mixer\n\n\n",
                             '''STR3="3246gt8456$%$^%" ## STR1="abc#123\n'''])

        with open('.env.empty', "w") as file:
            file.writelines("")

        with open('.env2', "w") as file:
            file.writelines(['''NUM1=-123\n\n''', "NUM2 = 118\n", '''NUM3=3246\n'''])

    def test_var(self):
        self.assertEqual(get_env_from_file(file_path=".env1"),
                         {'STR1': 'abc-123', 'STR2': 'mixer', 'STR3': '3246gt8456$%$^%'})
        self.assertEqual(get_env_from_file(file_path=".env2"),
                         {'NUM1': '-123', 'NUM2': '118', 'NUM3': '3246'})

    def test_empty_file(self):
        self.assertEqual(get_env_from_file(file_path=".env.empty"), {})

    def tearDown(self):
        os.remove(".env1")
        os.remove(".env2")
        os.remove(".env.empty")
