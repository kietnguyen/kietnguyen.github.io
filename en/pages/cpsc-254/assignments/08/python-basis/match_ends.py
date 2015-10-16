#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def match_ends(words):
    '''Given a list of strings, return the count of the number of strings where
    the string length is 2 or more and the first and last characters are the
    same.

    Note: python does not have a ++ operator, but += works.

    Keyword arguments:
    words -- a list of strings

    Return: number
    '''
    # +++your code here+++


def main():
    '''Main function for match_ends.py'''
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends([]), 0)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)


if __name__ == '__main__':
    main()
