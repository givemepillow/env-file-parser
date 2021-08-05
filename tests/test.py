import os
import sys
import unittest

# accessing to the parent directory
sys.path.append(os.path.dirname(os.getcwd()))

from source import get_env, get_envs


class TestGetEnv(unittest.TestCase):
    def setUp(self):
        with open('.env', "w") as file:
            file.writelines(['''CONST="abc-123"\n''', "NUMBER = 198"])

        with open('.env.comment', "w") as file:
            file.writelines(['''CONST="abc-123"\n''',
                             "# comment\n", "NUMBER = 198"])

        with open('../.env', "w") as file:
            file.writelines(['''CONST="abc-123"\n''', "NUMBER = 198"])

        with open('.env.conf', "w") as file:
            file.writelines(["CONST=adadsaskdjald\n", "NUMBER=-78"])

    def test_string_vars(self):
        self.assertEqual(get_env('CONST', file_path=f"{os.getcwd()}/.env"), 'abc-123')
        self.assertEqual(get_env('CONST', file_path=f"{os.getcwd()}/.env.conf"), 'adadsaskdjald')

    def test_vars_relative_path(self):
        self.assertEqual(get_env('CONST', file_path=".env"), 'abc-123')
        self.assertEqual(get_env('NUMBER', file_path=f"{os.getcwd()}/.env.conf"), '-78')

    def test_vars_with_comments(self):
        self.assertEqual(get_env('CONST', file_path=".env.comment"), 'abc-123')
        self.assertEqual(get_env('NUMBER', file_path=".env.comment"), '198')

    def test_key_error(self):
        with self.assertRaises(KeyError):
            get_env('NUM', file_path=f"{os.getcwd()}/.env")

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            get_env('NUM', file_path=f"{os.getcwd()}/.env.env")

    def tearDown(self):
        os.remove(f"{os.getcwd()}/.env")
        os.remove(f"{os.getcwd()}/.env.comment")
        os.remove(f"{os.getcwd()}/.env.conf")
        os.remove("../.env")


class TestGetEnvs(unittest.TestCase):
    def setUp(self):
        with open('.env.multi1', "w") as file:
            file.writelines(['''STR1="abc-123"\n''', "STR2 = mixer\n", '''STR3="3246gt8456$%$^%"\n'''])

        with open('.env.multi2', "w") as file:
            file.writelines(['''NUM1=-123\n''', "NUM2 = 118\n", '''NUM3=3246\n'''])

    def test_multi_vars(self):
        self.assertEqual(get_envs('STR1', 'STR2', 'STR3', file_path=f"{os.getcwd()}/.env.multi1"),
                         ['abc-123', 'mixer', '3246gt8456$%$^%'])
        self.assertEqual(get_envs('NUM1', 'NUM2', 'NUM3', file_path=f"{os.getcwd()}/.env.multi2"),
                         ['-123', '118', '3246'])

    def test_multi_key_error(self):
        with self.assertRaises(KeyError):
            get_envs('NUM', 'NUM2', 'NUM3', file_path=f"{os.getcwd()}/.env.multi2")

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            get_envs('NUM', file_path=f"{os.getcwd()}/.env.env")

    def tearDown(self):
        os.remove(f"{os.getcwd()}/.env.multi1")
        os.remove(f"{os.getcwd()}/.env.multi2")


if __name__ == '__main__':
    unittest.main()
