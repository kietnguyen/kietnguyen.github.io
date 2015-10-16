#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def mix_up(a, b):
    '''Given strings a and b, return a single string with a and b seperated
    by a space '<a> <b>', except swapping the first 2 characters of each
    string.

    Restriction:
    Both strings a and b must have at least length of 2.

    For example:
        mix_up('mix', 'pod') returns 'pox mid'

    Keyword arguments:
    a,b -- arbitrary strings

    Return: string
    '''
    # +++your code here+++


if __name__ == '__main__':
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
