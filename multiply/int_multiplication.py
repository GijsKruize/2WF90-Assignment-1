from subtraction.int_subtraction import *


def multiplication(radix: int, x: str, y: str) -> str:
    minus = ''
    if x.startswith('-') or y.startswith('-'):
        if not (x.startswith('-') and y.startswith('-')):
            minus = '-'

        y = y.replace('-', '')
        x = x.replace('-', '')

    x = x[::-1]
    y = y[::-1]

    max_x = len(x)
    max_y = len(y)
    answer = [0] * (len(x)+len(y))
    for i in range(0, max_x):
        carry = 0
        for j in range(0, max_y):
            digitx = convert_from_hex(x[i])
            digitY = convert_from_hex(y[j])

            t = int(convert_from_hex(answer[i + j])) + \
                int(digitx) * int(digitY) + carry
            carry = int(t / radix)
            answer[i + j] = str(convert_to_hex(t - (carry * radix)))

        answer[i + max_y] = str(convert_to_hex(carry))

    if answer[max_y + max_x - 1] == "0":
        k = max_y + max_x
    else:
        k = max_y + max_x

    answer = answer[:k]
    answer = answer[::-1]
    answer = ''.join(answer)
    return minus + answer.lstrip("0")
