#!/usr/bin/python3
"""
You have n number of locked boxes.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
The goal to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
