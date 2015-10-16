def test(got, expected):
    '''Simple test to print what each function returns vs. what it's
    supposed to return.
    '''
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(('%s got: %s - expected: %s' % (prefix, repr(got), repr(expected))))
