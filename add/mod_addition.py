
from helpers import is_positive
from reduction.mod_reduction import mod_reduction
from add.int_addition import addition
from subtraction.int_subtraction import subtraction


def mod_addition(radix, x, y, m):
    if (m == "0"):
        return None

    x = mod_reduction(radix, x, m)
    y = mod_reduction(radix, y, m)

    if (y == "0"):
        return x

    z_prime = addition(radix, x, y)
    if is_positive(subtraction(radix, z_prime, m)):
        return mod_reduction(radix, z_prime, m)

    return subtraction(radix, z_prime, m)
