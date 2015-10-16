#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def sum_exponents(nums, base):
    '''Given a list of numbers `nums` and an integer `base`, return the sum of
    each number times the `base` raised to the power of that number's index.

    For example: sum([1,2,3], 4) = 1 * 4^0 + 2 * 4^1 + 3 * 4^2 = 57
    See other test cases in main function.

    Note: In python, to calculate exponents, use ** operator.

    Keyword arguments:
    nums -- a list of numbers
    base -- an integer

    Return: number
    '''
    # +++your code here+++


def main():
    print('sum_exponents')
    test(sum_exponents([1, 2, 3], 4), 57)
    test(sum_exponents([], 3), 0)
    test(sum_exponents([1, 0, 1], 2), 5)
    test(sum_exponents([1, 3, 5], 8), 345)
    test(sum_exponents([2, 7, 1, 0, 9, 10], 16), 11075954)


if __name__ == '__main__':
    main()
