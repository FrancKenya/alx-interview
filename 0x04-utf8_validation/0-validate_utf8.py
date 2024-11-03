#!/usr/bin/python3
"""A method that checks if a given data set is a valid UTF-8 encoding"""


def validUTF8(data):
    """
    The function checking the data type
    Args:
        data (list): list of integers
    Return:
        True if data is a valid UTF-8 encoding
        False if data is not a valid UTF-8 encoding
    """
    num_bytes = 0  # Tracks remaining bytes in the UTF-8 character

    # Masks for checking UTF-8 encoding
    masks = [
        (0b11110000, 0b11110000),  # 4-byte character (11110xxx)
        (0b11100000, 0b11100000),  # 3-byte character (1110xxxx)
        (0b11000000, 0b11000000)   # 2-byte character (110xxxxx)
    ]
    continuation_mask = 0b11000000
    continuation_prefix = 0b10000000

    for byte in data:
        # Mask only the 8 least significant bits (one byte)
        byte = byte & 0xFF

        if num_bytes == 0:
            # New character - determine number of bytes
            if (byte & 0b10000000) == 0:
                # 1-byte character (ASCII, starts with '0xxxxxxx')
                continue
            elif (byte & masks[0][0]) == masks[0][1]:
                # 4-byte character (11110xxx)
                num_bytes = 3
            elif (byte & masks[1][0]) == masks[1][1]:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & masks[2][0]) == masks[2][1]:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            else:
                # Invalid starting byte
                return False
        else:
            # Continuation byte check (should start with '10')
            if (byte & continuation_mask) != continuation_prefix:
                return False
            num_bytes -= 1

    # If num_bytes is 0, all characters matched the UTF-8 format
    return num_bytes == 0
