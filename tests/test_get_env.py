import os
import unittest

from source import get_env


class TestGetEnv(unittest.TestCase):
    def setUp(self):
        with open('.env.empty', "w") as file:
            file.writelines("")

        with open('.env', "w") as file:
            file.write('''\n'''
                       '''# The env file\n'''
                       '''CONST = "abc-123" # comment for const\n'''
                       '''NUMBER = -12345 # 'this is number' \n'''
                       """Q = '"' # 'text' \n"""
                       )

        with open('../.env', "w") as file:
            file.write(
                '''CONST="rel"\n'''
                "NUMBER = 198"
            )

        with open('.env.conf', "w") as file:
            file.write(
                "CONST=aa##aa\n"
                "NUMBER='-78' # NUMBER = '-78'\n"
            )

    def test_string_vars(self):
        self.assertEqual(get_env('CONST', file_path=".env"), 'abc-123')
        self.assertEqual(get_env('CONST', file_path=".env.conf"), 'aa')
        self.assertEqual(get_env('Q', file_path=".env"), '"')

    def test_vars_relative_path(self):
        self.assertEqual(get_env('CONST', file_path="../.env"), 'rel')
        self.assertEqual(get_env('NUMBER', file_path="../.env"), '198')

    def test_key_error(self):
        with self.assertRaises(KeyError):
            get_env('NUM', file_path=".env")
            get_env('CONST', file_path=".env.empty")

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            get_env('NUM', file_path=".env.not")

    def tearDown(self):
        os.remove(".env")
        os.remove(".env.conf")
        os.remove("../.env")
        os.remove(".env.empty")
