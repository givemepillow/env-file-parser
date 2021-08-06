import os
import unittest

from source import get_envs


class TestGetEnvs(unittest.TestCase):
    def setUp(self):
        with open('.env.multi1', "w") as file:
            file.writelines(['''STR1="abc-123"\n\n''', "STR2 = mixer\n\n\n", '''STR3="3246gt8456$%$^%"\n'''])

        with open('.env.multi2', "w") as file:
            file.writelines(['''NUM1=-123\n\n''', "NUM2 = 118\n", '''NUM3=3246\n'''])

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