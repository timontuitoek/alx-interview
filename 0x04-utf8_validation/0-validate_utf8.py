#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.

Usage: utf8_validator.py < filename
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Function checks if a given number
    # is a valid start of a UTF-8 character
    def valid_start(byte):
        return bin(byte).startswith('0b' + '1' * (8 - length) + '0' * (length - 1))

    length = 0  # Number of remaining bytes to read for current character
    for byte in data:
        if length == 0:  # Start of a new character
            if byte >> 5 == 0b110:
                length = 1
            elif byte >> 4 == 0b1110:
                length = 2
            elif byte >> 3 == 0b11110:
                length = 3
            elif byte >> 7 == 1:  # Single byte character
                continue
            else:
                return False
        else:  # Inside a multi-byte character
            if byte >> 6 != 0b10:  # Check if byte is of form 10xxxxxx
                return False
            length -= 1
    return length == 0  # Check if all characters have been properly terminated
