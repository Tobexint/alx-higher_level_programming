#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """
    Reads from filename and prints
    its contents to stdout.
    Args:
     - filename: name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
