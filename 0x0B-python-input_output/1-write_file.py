#!/usr/bin/python3
""" Module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
