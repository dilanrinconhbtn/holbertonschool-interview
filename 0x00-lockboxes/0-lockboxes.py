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
        if(boxes[0]):
            while(counter != max_boxes):

                if(len(boxes[box_key[counter]])):
                    for x in range(0, len(boxes[box_key[counter]])):
                        for check in box_key:
                            if(check != boxes[box_key[counter]][x]):
                                flag = 0
                            else:
                                flag = 1
                                break
                        if(flag == 0):
                            box_key.append(boxes[box_key[counter]][x])
                    counter = counter + 1
                else:
                    break
    if len(box_key) == max_boxes:
        return True
    else:
        return False
