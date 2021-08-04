import os
import unittest

from source import get_env

class TestGetEnv(unittest.TestCase):
    def test_string_vars(self):
        self.assertEqual(get_env('CONST'), 'abc-123')
        self.assertEqual(get_env('CONST', file_path='.env.conf'), 'adadsaskdjald')

    def test_numbers_vars(self):
        self.assertEqual(get_env('NUMBER'), 198)
        self.assertEqual(get_env('NUMBER', file_path='.env.conf'), -78)


if __name__ == '__main__':
    with open('.env', "w") as file:
        file.writelines(['''CONST="abc-123"\n''', "NUMBER = 198"])

    with open('.env.conf', "w") as file:
        file.writelines(["CONST=adadsaskdjald\n", "NUMBER=-78"])
    unittest.main()
    os.remove('.env.conf')
    os.remove('.env')
