from reduction.mod_reduction import mod_reduction
from multiply.int_multiplication import multiplication


def mod_multiplication(radix: int, x: str, y: str, modulus: str) -> str:
    y = mod_reduction(radix, y, modulus)
    x = mod_reduction(radix, x, modulus)

    return mod_reduction(radix, multiplication(radix, x, y), modulus)
