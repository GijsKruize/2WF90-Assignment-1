from typing import Tuple
from helpers import absolute, is_at_least_zero, is_positive, division_with_remainder
from multiply.int_multiplication import multiplication
from subtraction.int_subtraction import subtraction


def extended_euclidian(radix: int, a: str, b: str) -> Tuple[str, str, str]:
    a_prime = absolute(a)
    b_prime = absolute(b)

    x_1 = "1"
    x_2 = "0"
    y_1 = "0"
    y_2 = "1"

    while is_positive(b_prime):
        q, r = division_with_remainder(radix, a_prime, b_prime)

        a_prime = b_prime
        b_prime = r

        x_3 = subtraction(radix, x_1, multiplication(radix, q, x_2))
        y_3 = subtraction(radix, y_1, multiplication(radix, q, y_2))

        x_1 = x_2
        y_1 = y_2

        x_2 = x_3
        y_2 = y_3

    d = a_prime

    x = x_1 if is_at_least_zero(a) else "-" + x_1
    y = y_1 if is_at_least_zero(a) else "-" + y_1

    return (d, x, y)
