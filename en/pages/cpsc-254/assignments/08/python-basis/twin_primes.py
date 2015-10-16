#!/usr/bin/python3

'''CPSC 254 - Assignment 08'''

from test import test
import math


def get_primes(max_num):
    '''Given an positive integer number `max_num`, return a list of all prime
    number that is less than or equal to `max_num`.

    Note: You don't need to check wheter `max_num` is an positive integer.

    Keyword arguments:
    max_num -- an positive integer

    Return: a list of primes
    '''
    # +++your code here+++


def get_twin_primes(primes):
    '''Given a list of prime numbers, return a list of tuples of two twin
    primes, which are prime numbers that differ from each other by 2.

    Keyword arguments:
    primes -- list of prime numbers

    Return: a list of tuples of two twin primes
    '''
    # +++your code here+++


def test_get_primes():
    '''To test get_primes function.

    Keyword arguments: None

    Return: None
    '''
    print('get_primes')
    test(get_primes(1), [])
    test(get_primes(2), [2])
    test(get_primes(10), [2, 3, 5, 7])
    test(get_primes(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


def test_get_twin_primes():
    '''To test get_twin_primes function.

    Keyword arguments: None

    Return: None
    '''
    print('twin_primes')
    primes = get_primes(100)
    test(get_twin_primes([2, 3]), [])
    test(get_twin_primes(primes),
         [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31),
          (41, 43), (59, 61), (71, 73)])


def main():
    '''Main function for twin_primes.py'''
    test_get_primes()
    test_get_twin_primes()


if __name__ == '__main__':
    main()
