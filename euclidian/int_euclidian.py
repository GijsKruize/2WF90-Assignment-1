from typing import Tuple
from helpers import *
from karatsuba.int_karatsuba import karatsuba
from subtraction.int_subtraction import subtraction


def extended_euclidian(radix: int, a: str, b: str) -> Tuple[str, str, str]:
    a_prime = absolute(a)
    b_prime = absolute(b)

    x_1 = "1"
    x_2 = "0"
    y_1 = "0"
    y_2 = "1"

    while is_positive(b_prime):
        q, r = long_division(radix, a_prime, b_prime)

        a_prime = b_prime
        b_prime = r

        x_3 = subtraction(radix, x_1, karatsuba(radix, q, x_2))
        y_3 = subtraction(radix, y_1, karatsuba(radix, q, y_2))

        x_1 = x_2
        y_1 = y_2

        x_2 = x_3
        y_2 = y_3

    d = a_prime

    x = x_1 if is_at_least_zero(a) else "-" + x_1
    y = y_1 if is_at_least_zero(a) else "-" + y_1

    return (d, x, y)


def long_division(radix: int, x: str, y: str) -> Tuple[str, str]:
    q = ""
    r = ""

    answer_should_be_negative = not is_at_least_zero(x)

    x = absolute(x)
    y = absolute(y)

    for i in range(len(x)):
        r = r.lstrip("0") + x[i]

        # Primary school long division:
        # As long as r - y is not negative, it is possible to divide r by y
        # else add a 0 to basically multiply by the radix
        if (is_at_least_zero(subtraction(radix, r, y))):
            # Calculate how often y fits into r
            largest_q = largest_quotient(radix, r, y)
            # Append this largest quotient to q
            q = q + largest_q

            # Calculate the current remainder by multipying y by the
            # largest quotient and then subtracting that from the current position in x
            temp = karatsuba(radix, y, largest_q)
            r = subtraction(radix, r, karatsuba(radix, y, largest_q))
        else:
            # if we cannot divide, add a 0 to basically multiply q by the radix
            q = q + "0"

    q = remove_leading_zeros(q)

    if (is_positive(q) and answer_should_be_negative):
        q = "-" + q

    return (q, r)


# Calculate how many times you can divide y by r
def largest_quotient(radix: int, r: str, y: str) -> str:
    from add.int_addition import addition
    q_prime = 0
    y_prime = "0"

    for i in range(1, radix):
        y_prime = addition(radix, y_prime, y)

        if is_at_least_zero(subtraction(radix, r, y_prime)):
            q_prime = i
        else:
            break

    return get_representation(q_prime)
