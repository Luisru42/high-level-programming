#! /usr/bin/env python3
"""Module for reading a specific number of lines from a text file."""


def read_lines(filename="", nb_lines=0):
    """Reads a specified number of lines from a text file.

    Args:
    filename (str): The name of the file to read. Defaults to an empty string.
    nb_lines (int): The number of lines to read from the file. Defaults to 0.

    Returns:
        str: The content of the read lines.
    """
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            return file.read()
        return "".join(file.readline() for _ in range(nb_lines))
