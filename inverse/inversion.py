
from add.int_addition import addition
from euclidian.int_euclidian import extended_euclidian
from helpers import is_at_least_zero
from reduction.mod_reduction import mod_reduction


def inversion(radix, x, mod):
    g, a, y = extended_euclidian(radix, x, mod)

    # if (g != 1):
    #     return None

    # else:
    a = mod_reduction(radix, a, mod)

    if not is_at_least_zero(a):
        a = addition(radix, a, mod)
        return a
