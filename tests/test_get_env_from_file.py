import os
import unittest

from source import get_env_from_file


class TestGetEnvFromFile(unittest.TestCase):
    def setUp(self):
        with open('.env1', "w") as file:
            file.writelines(['''STR1="abc-123"\n\n''', "STR2 = mixer\n\n\n", '''STR3="3246gt8456$%$^%" # hello\n'''])

        with open('.env.empty', "w") as file:
            file.writelines("")

        with open('.env2', "w") as file:
            file.writelines(['''NUM1=-123\n\n''', "NUM2 = 118\n", '''NUM3=3246\n'''])

    def test_multi_vars(self):
        self.assertEqual(get_env_from_file('STR1', 'STR2', 'STR3', file_path=f"{os.getcwd()}/.env1"),
                         ['abc-123', 'mixer', '3246gt8456$%$^%'])
        self.assertEqual(get_env_from_file('NUM1', 'NUM2', 'NUM3', file_path=f"{os.getcwd()}/.env2"),
                         ['-123', '118', '3246'])

    def test_single_var(self):
        self.assertEqual(get_env_from_file('STR1', file_path=f"{os.getcwd()}/.env1"), 'abc-123')
        self.assertEqual(get_env_from_file('NUM3', file_path=f"{os.getcwd()}/.env2"), '3246')

    def test_no_one_var(self):
        self.assertEqual(get_env_from_file(file_path=f"{os.getcwd()}/.env1"),
                         {'STR1': 'abc-123', 'STR2': 'mixer', 'STR3': '3246gt8456$%$^%'})
        self.assertEqual(get_env_from_file(file_path=f"{os.getcwd()}/.env2"),
                         {'NUM1': '-123', 'NUM2': '118', 'NUM3': '3246'})

    def test_empty_file(self):
        with self.assertRaises(KeyError):
            get_env_from_file('NUM', 'NUM2', 'NUM3', file_path=f"{os.getcwd()}/.env.empty")
        self.assertEqual(get_env_from_file(file_path=f"{os.getcwd()}/.env.empty"), {})

    def test_multi_key_error(self):
        with self.assertRaises(KeyError):
            get_env_from_file('NUM', 'NUM2', 'NUM3', file_path=f"{os.getcwd()}/.env2")

    def test_key_error(self):
        with self.assertRaises(KeyError):
            get_env_from_file('NUM4', file_path=f"{os.getcwd()}/.env2")
            get_env_from_file('CONST', file_path=f"{os.getcwd()}/.env.empty")

    def tearDown(self):
        os.remove(f"{os.getcwd()}/.env1")
        os.remove(f"{os.getcwd()}/.env2")
        os.remove(f"{os.getcwd()}/.env.empty")
