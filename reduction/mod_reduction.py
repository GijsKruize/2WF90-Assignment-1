
from euclidian.int_euclidian import long_division


def mod_reduction(radix: int, x: str, modulus: str) -> str:
    return long_division(radix, x, modulus)[1]
