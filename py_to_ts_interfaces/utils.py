import re


def to_camel_case(snake_str: str) -> str:
    """
    Convert a snake_case string to camelCase.

    :param snake_str: The input in snake_case.
    :return: The input, but in camelCase.
    """
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    return components[0] + ''.join(x.title() for x in components[1:])
    # with the 'title' method and join them together.


def is_from_statement(line: str) -> bool:
    """
    Check if the given string is a from statement, e.g. "from typing import List"

    :param line: The string to check (should be one line of code).
    :return: True if the given string is a from statement.
    """
    return line.startswith("from ") and "import" in line


def is_class_definition(line: str) -> bool:
    """
    Check if the given string is a class definition, e.g. "class MyInterface:"

    :param line: The string to check (should be one line of code).
    :return: True if the given string is a class definition.
    """
    return line.startswith("class ")


def is_string_definition(line: str) -> bool:
    """
    Check if the given string is a string definition. Ignores type hints such as Final.
    e.g. CONSTANT_STRING: Final = "example"

    :param line: The string to check (should be one line of code).
    :return: True if the given string is a string definition.
    """
    return re.match("[a-zA-Z_]+.* = \".*\"", line) is not None


def is_comment_definition(line: str) -> bool:
    """
    Check if the given string is a comment definition. e.g. # This is a comment

    :param line: The string to check (should be one line of code).
    :return: True if the given string is a comment definition.
    """

    return re.match("\s*#.*", line) is not None