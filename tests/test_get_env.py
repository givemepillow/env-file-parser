import os
import unittest

from source import get_env


class TestGetEnv(unittest.TestCase):
    def setUp(self):
        with open('.env.empty', "w") as file:
            file.writelines("")

        with open('.env', "w") as file:
            file.writelines(['''CONST=" abc-123     "\n''',
                             '''"abc-123"\n''', "NUMBER = 198"])

        with open('.env.comment1', "w") as file:
            file.writelines(['''CONST="abc-123"\n''',
                             "# comment\n", "NUMBER = 198"])

        with open('.env.comment2', "w") as file:
            file.writelines(['''CONST="abc-#123"\n\n''',
                             "# comment\n", "NUMBER = 198#comment"])

        with open('.env.comment3', "w") as file:
            file.writelines(['''CONST1="abc-#123"# this is const\n\n''',
                             '''CONST2 = "abc#-#123" # the ### const\n\n''',
                             "# comment\n\n", "NUMBER = 198#comment # for num"])

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
        self.assertEqual(get_env('CONST', file_path=".env.comment1"), 'abc-123')
        self.assertEqual(get_env('NUMBER', file_path=".env.comment1"), '198')
        self.assertEqual(get_env('CONST', file_path=".env.comment2"), 'abc-#123')
        self.assertEqual(get_env('NUMBER', file_path=".env.comment2"), '198')
        self.assertEqual(get_env('CONST1', file_path=".env.comment3"), 'abc-#123')
        self.assertEqual(get_env('NUMBER', file_path=".env.comment3"), '198')
        self.assertEqual(get_env('CONST2', file_path=".env.comment3"), 'abc#-#123')

    def test_key_error(self):
        with self.assertRaises(KeyError):
            get_env('NUM', file_path=f"{os.getcwd()}/.env")
            get_env('CONST', file_path=f"{os.getcwd()}/.env.empty")

    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            get_env('NUM', file_path=f"{os.getcwd()}/.env.env")

    def tearDown(self):
        os.remove(f"{os.getcwd()}/.env")
        os.remove(f"{os.getcwd()}/.env.comment1")
        os.remove(f"{os.getcwd()}/.env.comment2")
        os.remove(f"{os.getcwd()}/.env.comment3")
        os.remove(f"{os.getcwd()}/.env.conf")
        os.remove("../.env")
        os.remove(f"{os.getcwd()}/.env.empty")
