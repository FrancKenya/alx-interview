#!/usr/bin/python3

"""Function opens a stack of boxes and returns true if all opened
and false if not all opened"""


def canUnlockAll(boxes):
    """Function that checks if n number of boxes can be all opened
    Returns: True if they are all successfully opened and False if not"""

    # create a set for rhe opened boxes with the first box
    opened_boxes = {0}
    # make a shallow copy stack of opened box 0 content
    list_1 = boxes[0].copy()

    # check if there is the copy is not empty and pop the last to use
    while list_1:
        key = list_1.pop()
        # check if key matches a box and not used yet
        if key not in opened_boxes and key < len(boxes):
            # Add it to the set of opened boxes
            opened_boxes.add(key)
            # Add all keys found to the stack
            list_1.extend(boxes[key])
    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
