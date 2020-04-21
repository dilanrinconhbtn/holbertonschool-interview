#!/usr/bin/python3
""" Unlock the boxes
"""


def canUnlockAll(boxes):
    """
    Unlock all boxes
    boxes: list with another lists inside that contein keys
    """
    box_key = [0]
    max_boxes = len(boxes)
    counter = 0
    if(boxes):
        while(counter != max_boxes):
            if(len(box_key) > counter):
                if(len(boxes[box_key[counter]]) > 0):
                    for x in range(0, len(boxes[box_key[counter]])):
                        if(boxes[box_key[counter]][x] not in box_key):
                            if(max_boxes > boxes[box_key[counter]][x]):
                                box_key.append(boxes[box_key[counter]][x])
                    counter = counter + 1
                else:
                    break
            else:
                break
    if len(box_key) == max_boxes:
        return True
    else:
        return False
