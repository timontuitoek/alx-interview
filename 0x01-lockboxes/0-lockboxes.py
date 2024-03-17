#!/usr/bin/python3
"""def canUnlockAll(boxes):"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    keys_to_check = [0]

    while keys_to_check:
        box_index = keys_to_check.pop()
        keys = boxes[box_index]
        for key in keys:
            if 0 <= key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys_to_check.append(key)

    return all(unlocked)


# Example usage:
if __name__ == "__main__":
    # Example boxes:
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output should be True
