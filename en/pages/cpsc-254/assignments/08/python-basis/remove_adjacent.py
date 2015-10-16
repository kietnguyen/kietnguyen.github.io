#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def remove_adjacent(nums):
    '''Given a list of numbers, return a list where all adjacent same elements
    have been reduced to a single element.

    For example:
        remove_adjacent([1, 2, 2, 3]) returns [1, 2, 3]

    Keyword arguments:
    nums -- a list of numbers

    Return: list
    '''
    # +++your code here+++


if __name__ == '__main__':
    print('remove_adjacent')
    test(remove_adjacent([2, 1, 1, 3]), [2, 1, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([2, 1, 1, 2, 2]), [2, 1, 2])
    test(remove_adjacent([0]), [0])
    test(remove_adjacent([]), [])
