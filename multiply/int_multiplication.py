# TODO delete substition for unfinished work for running tests

from math import floor

from helpers import *


def multiplication(radix, x, y):
    # Zero times something is still zero.
    if (x == "0" or y == "0"):
        return "0"

    #check if the input x and y have a minus sign in front of them. If both of them have one, the result won't have one.
    #If one of them has one the result will be calculated without the minus and the answer will change sign.
    if (x.startswith("-") and y.startswith("-")):
        # A negative number (`x`) times another negative number (`y`) is positive.
        return multiplication(radix, x[1:], y[1:])
    elif (x.startswith("-")):
        # A negative number (`x`) times a positive number (`y`) is the same as
        # a positive number times a positive number and inverting the sign.
        outcome = multiplication(radix, x[1:], y)
        return "-" + outcome
    elif (y.startswith("-")):
        # A positive number (`x`) times a negative number(`x`) is the same as
        # a positive number times a positive number and inverting the sign.
        outcome = multiplication(radix, x, y[1:])
        return "-" + outcome

    # Now the multiplication part starts with two positive numbers 'x' and 'y'
    # Initialization
    m = len(x)
    n = len(y)

    # Create an array which holds the answer, it has one extra cell for a
    # possible carry-out.
    z = ["0"] * (m + n)
    count_add = 0
    count_mul = 0

    # Reverse `x` and `y` to accomodate for reversed indexing in algorith.
    x = x[::-1]
    y = y[::-1]

    for i in range(m):
        carry = 0

        for j in range(n):
            # Determine the expected value of the "character" multiplication.
            expected_word = get_key(z[i + j]) + \
                (get_key(x[i]) * get_key(y[j])) + carry
            count_add += 2
            count_mul += 1

            # Determine the `carry`, `expected_word` is never larger than 32 bits
            # thus we can use elementary division.
            carry = floor(expected_word / radix)

            # Subtract what is too much.
            z[i + j] = get_representation(expected_word - (carry * radix))
            count_mul += 1
        # And carry-out.
        z[i + n] = get_representation(carry)

    # Reverse string and strip any leading zero (carry-out). If the string is
    # empty, make the string a zero ("0").
    result = (''.join(i for i in z[::-1])).lstrip("0")
    if (len(result) == 0):
        result = "0"

    # Return the answer, the number of elementary additions, and the number of
    # elementary multiplications.
    return result
