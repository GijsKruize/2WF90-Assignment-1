
from euclidian.int_euclidian import long_division
from typing import Optional


def mod_reduction(radix: int, x: str, modulus: str) -> Optional[str]:
    if (modulus == "0"):
        return None

    return long_division(radix, x, modulus)[1]
