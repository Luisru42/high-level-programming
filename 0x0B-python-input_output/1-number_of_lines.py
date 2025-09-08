#! /usr/bin/env python3
"""Module for counting the number of lines in a text file."""


def number_of_lines(filename=""):
    """Counts the number of lines in a text file.

    Args:
    filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        int: The number of lines in the file.
    """
    with open(filename, encoding="utf-8") as file:
        return sum(1 for line in file)
