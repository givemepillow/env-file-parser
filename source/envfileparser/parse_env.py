def parse_env(env_file_lines: list) -> dict:
    """A function that extracts a variable from a list of strings.

    Each line from the list is divided by the first equal sign.
    The left part is taken for the variable name,
    and the right part is taken for the value.
    Empty lines, lines starting with " # " and
    lines without '=' are skipped. Comments to the
    right of the code are deleted.
    The value will always be stored as a string.

    :param env_file_lines: list of lines
    :type env_file_lines: list
    :return: dict var name - var value
    """
    env_vars = {}
    for line in env_file_lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#' or '=' not in line:
            continue

        equal_index = line.index('=')
        value = line[equal_index + 1::].strip()

        if '#' in value:
            if value[0] in ("'", '''"'''):
                if value[::-1].index(value[0]) > value.index('#'):
                    value = value[0:value.index('#')]
            else:
                value = value[0:value.index('#')]

        # Remove the quotation marks, if there are any.
        if value[0] == value[-1] and value[0] in ('''"''', """'"""):
            value = value[1:len(value) - 1]
        key = line[0:equal_index].strip()
        env_vars[key] = value

    return env_vars
