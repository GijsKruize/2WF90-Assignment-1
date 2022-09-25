from subtraction.int_subtraction import subtraction
from reduction.mod_reduction import mod_reduction


def mod_subtraction(radix: int, x: str, y: str, m: str) -> str:
    x = mod_reduction(radix, x, m)
    y = mod_reduction(radix, y, m)
    z = subtraction(radix, x, y)
    z = mod_reduction(radix, z, m)

    return z
