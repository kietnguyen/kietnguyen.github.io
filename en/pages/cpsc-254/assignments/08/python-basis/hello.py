#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test


def hello(name):
    '''Print a greeting message "Hello [name]" (without quotes), where [name]
    is given by the argument `name` from the function.

    Keyword arguments:
    name -- a string

    Return: None
    '''
    # +++your code here+++


def main():
    # Just simple eyeball-testing to see the greeting message. When you execute
    # this program, you should see below output without any leading space.
    #   Hello Alice
    #   Hello Bob
    hello('Alice')
    hello('Bob')


if __name__ == '__main__':
    main()
