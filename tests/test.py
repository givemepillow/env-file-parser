import os

from source import get_env


def test_one():
    assert get_env('CONST', file_path=".env") == 'abc-123'
    print("Test one passed.")


def test_two():
    assert get_env('NUMBER') == 198
    print("Test two passed.")


def test_three():
    assert get_env('NUMBER', file_path='.env.conf') == -78
    print("Test three passed.")


def test_four():
    assert get_env('CONST', file_path='.env.conf') == 'adadsaskdjald'
    print("Test four passed.")


if __name__ == '__main__':
    with open('.env', "w") as file:
        file.writelines(['''CONST="abc-123"\n''', "NUMBER = 198"])

    with open('.env.conf', "w") as file:
        file.writelines(["CONST=adadsaskdjald\n", "NUMBER=-78"])

    test_one()
    test_two()
    test_three()
    test_four()
    os.remove('.env.conf')
    os.remove('.env')
