import os
import unittest

from source import get_env


class TestGetEnv(unittest.TestCase):
    def setUp(self):
        with open('.env', "w") as file:
            file.writelines(['''CONST="abc-123"\n''', "NUMBER = 198"])

        with open('.env.conf', "w") as file:
            file.writelines(["CONST=adadsaskdjald\n", "NUMBER=-78"])

    def test_string_vars(self):
        self.assertEqual(get_env('CONST', file_path=f"{os.getcwd()}\.env"), 'abc-123')
        self.assertEqual(get_env('CONST', file_path=f"{os.getcwd()}\.env.conf"), 'adadsaskdjald')

    def test_numbers_vars(self):
        self.assertEqual(get_env('NUMBER', file_path=f"{os.getcwd()}\.env"), 198)
        self.assertEqual(get_env('NUMBER', file_path=f"{os.getcwd()}\.env.conf"), -78)

    def tearDown(self):
        os.remove(f"{os.getcwd()}\.env")
        os.remove(f"{os.getcwd()}\.env.conf")

if __name__ == '__main__':
    unittest.main()

