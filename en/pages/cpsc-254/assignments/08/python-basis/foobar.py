#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def foobar(num):
    '''Given an integer num, return a string followed by these rules:
        - if that number is a multiple of 3, return 'foo';
        - if that number is a multiple of 7, return 'bar';
        - if that number is multiples of both 3 and 7, return 'foobar';
        - otherwise, return that number as a string;

    Keyword arguments:
    num -- an integer number

    Return: a string
    '''
    # +++your code here+++


def main():
    '''Main function for foobar.py'''
    print('foobar')
    test(foobar(1), '1')
    test(foobar(3), 'foo')
    test(foobar(7), 'bar')
    test(foobar(21), 'foobar')
    test(foobar(40), '40')


if __name__ == '__main__':
    main()
