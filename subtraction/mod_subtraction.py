from subtraction.int_subtraction import subtraction
from reduction.mod_reduction import mod_reduction
from typing import Optional
from add.int_addition import addition


def mod_subtraction(radix: int, x: str, y: str, m: str) -> Optional[str]:
    if (m == "0"):
        return None

    x = mod_reduction(radix, x, m)
    if x.startswith('-'):
        x = addition(radix, x, m)
    y = mod_reduction(radix, y, m)
    if y.startswith('-'):
        y = addition(radix, y, m)
    z = subtraction(radix, x, y)

    if z.startswith('-'):
        z = addition(radix, z, m)
    return z
