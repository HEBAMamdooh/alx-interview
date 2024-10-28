#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given list of integers represents valid [UTF-8] encoding.

    Args:
        data (List[int]): A list of integers where each integer 
        represents a byte (0-255).

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0
    
    # Masks for the bitwise operations
    # Mask to check if a byte starts with '10xxxxxx'
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    # Go through each integer (byte) in the data list
    for num in data:
        # Get the last 8 bits (we only care about one byte at a time)
        byte = num & 0xFF

        # If no bytes are remaining, this byte is the start of a new character
        if bytes_remaining == 0:
            # Check the number of leading 1's to determine the length
            if (byte >> 5) == 0b110:     # 110xxxxx => 2-byte character
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx => 3-byte character
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110: # 11110xxx => 4-byte character
                bytes_remaining = 3
            elif (byte >> 7):            # 1xxxxxxx => invalid must start with 0 
                return False
        else:
            # Check if byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
            # Decrease the count of bytes remaining
            bytes_remaining -= 1

    # All characters should be fully matched
    return bytes_remaining == 0
