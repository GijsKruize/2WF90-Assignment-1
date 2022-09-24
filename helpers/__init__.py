def is_positive(x: str) -> bool:
    x_stripped = remove_leading_zeros(x)

    if x_stripped == "0":
        return False

    return not x_stripped.startswith("-")


def is_at_least_zero(x: str) -> bool:
    return not x.startswith("-")

def remove_leading_zeros(x: str) -> str:
    x_stripped = x.lstrip("0")

    if x_stripped == "":
        return "0"

    return x_stripped
