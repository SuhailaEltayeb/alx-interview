#!/usr/bin/python3
"""
Check if all boxes can be unlocked based on available keys.
"""

def can_open_all_boxes(box_list):
    """
    Determines whether all boxes in a list can be unlocked using the keys available in each box.

    Args:
        box_list (list): A list of boxes where each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if not isinstance(box_list, list):
        return False
    if len(box_list) == 0:
        return False

    for key in range(1, len(box_list) - 1):
        key_found = False
        for box_index in range(len(box_list)):
            key_found = key in box_list[box_index] and key != box_index
            if key_found:
                break
        if not key_found:
            return False
    return True
