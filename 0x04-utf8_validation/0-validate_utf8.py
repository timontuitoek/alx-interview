#!/usr/bin/python3
"""
Defines a function that determines whether a list of
integers passed into it conforms to UTF-8 format.
"""
from itertools import takewhile


def int_to_bits(nums):
    """
    Helper function
    Converts integers to binary representations.
    """
    for num in nums:
        bits = []
        mask = 1 << 8  # Because there are 8 bits per byte
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits


def validUTF8(data):
    """
    Takes a list of integers and returns True if the list is
    a valid UTF-8 encoding, else returns False.
    Args:
        data : List of integers representing a possible UTF-8 encoding
    Returns:
        bool : True if valid UTF-8, False otherwise
    """
    bits = int_to_bits(data)

    for byte in bits:
        # If single-byte character, it's valid. Continue.
        if byte[0] == 0:
            continue

        # If here, the byte is a multi-byte character.
        ones = sum(takewhile(bool, byte))

        # Check if the number of leading ones is within valid UTF-8 range.
        if ones <= 1 or ones >= 4:  # UTF-8 can be 1 to 4 bytes long
            return False

        # Check the next bytes in the sequence for the expected pattern.
        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False

            # Check if the byte starts with "10" in binary.
            if byte[0:2] != [1, 0]:
                return False

    return True
