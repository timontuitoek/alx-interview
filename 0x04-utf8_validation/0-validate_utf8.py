#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """

    def valid_start(byte):
        return bin(byte).startswith
    ('0b' + '1' * (8 - length) + '0' * (length - 1))

    length = 0  # Number of remaining bytes
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
        else:
            if byte >> 6 != 0b10:
                return False
            length -= 1
    return length == 0
