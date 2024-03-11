#!/usr/bin/python3
"""
def pascal_triangle(n)
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    """ initialize an empty resulting array """
    pascal_list = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if (col < li):
                if (col == 0):
                    """ the first column is always set to 1 """
                    pascal_list[li].append(1)
                else:
                    pascal_list[li].append(
                        pascal_list[li-1][col] + pascal_list[li-1][col-1])
            elif (col == li):
                """ the diagonal is always set to 1 """
                pascal_list[li].append(1)

    return pascal_list
