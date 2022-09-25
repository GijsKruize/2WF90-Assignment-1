from typing import Tuple
from add.int_addition import addition
from subtraction.int_subtraction import subtraction
from multiply.int_multiplication import multiplication


REPRESENTATIONS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
                   7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
KEYS = {v: k for k, v in REPRESENTATIONS.items()}


def get_representation(x: int) -> str:
    return REPRESENTATIONS[x]


def get_key(x: str) -> int:
    return KEYS[x.lower()]


def remove_leading_zeros(x: str) -> str:
    x_stripped = x.lstrip("0")

    if x_stripped == "":
        return "0"

    return x_stripped


def is_positive(x: str) -> bool:
    x_stripped = remove_leading_zeros(x)

    if x_stripped == "0":
        return False

    return not x_stripped.startswith("-")


def is_at_least_zero(x: str) -> bool:
    return not x.startswith("-")


def absolute(x: str) -> str:
    return x[1:] if x[0] == "-" else x


def get_length(x: str) -> int:
    x_absolute = absolute(x)

    return len(remove_leading_zeros(x_absolute))


def radix_to_decimal(radix: int, x: str) -> int:
    is_negative = not is_at_least_zero(x)
    x_absolute = absolute(x)

    decimal = 0

    for i in range(len(x_absolute)):
        decimal += get_key(x_absolute[len(x_absolute) - 1 - i]) * radix ** i

    return -decimal if is_negative else decimal


def division_with_remainder(radix: int, x: str, y: str) -> Tuple[str, str]:
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
            r = subtraction(radix, r, multiplication(radix, y, largest_q))
        else:
            # if we cannot divide, add a 0 to basically multiply q by the radix
            q = q + "0"

    q = remove_leading_zeros(q)

    if (is_positive(q) and answer_should_be_negative):
        q = "-" + q

    return (q, r)


def largest_quotient(radix: int, r: str, y: str) -> str:
    q_prime = 0
    y_prime = "0"

    for i in range(1, radix):
        y_prime = addition(radix, y_prime, y)

        if (not str(subtraction(radix, r, y_prime)[0]).startswith("-")):
            q_prime = i
        else:
            break

    return get_representation(q_prime)
