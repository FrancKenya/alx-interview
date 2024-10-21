#!/usr/bin/python3

""" A function that  displays the functionality of
a minimum operations program """


def minOperations(n):
    """
    A function that calculates the fewest number of
    operations needed to result in exactly n H
    characters in a file.
    Returns: An integer
        If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    # initialize operations
    operations = 0
    # use the least prime number(not 1 as it does not make any change
    # dividing a number by 1) as the divisor
    divisor = 2

    # start  a loop to check for divisibility and reduce n
    while n > 1:
        # check if it is divisible by our divisor
        while n % divisor == 0:
            # make the operation
            operations += divisor
            # update the value of n after an operation and
            # round it to a whole number
            n //= divisor
        # Add 1 if n not divisible by our divisor and try again
        divisor += 1
    return operations
