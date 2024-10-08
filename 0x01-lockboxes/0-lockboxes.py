#!/usr/bin/python3
"""
Solving LockBoxes Dialemma
"""


def canUnlockAll(boxes):
    """
    Method to determines if all the boxes can be opened
    based on keys given.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        boxes_checked = False
        for indx in range(len(boxes)):
            checked_boxes = key in boxes[indx] and key != indx
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
