from helpers import *


def bigger_y_than_x(x, y):
    i = 0
    while i < len(x):
        NumberX = get_key(x[i])
        NumberY = get_key(y[i])

        if NumberX > NumberY:
            return False
        elif NumberY > NumberX:
            return True
        i = i+1
    return False


def convert_from_hex(digit):
    if digit == 'A':
        return 10

    elif digit == 'B':
        return 11

    elif digit == 'C':
        return 12

    elif digit == 'D':
        return 13

    elif digit == 'E':
        return 14

    elif digit == 'F':
        return 15

    elif digit == 'G':
        return 16
    else:
        return int(digit)


def convert_to_hex(digit):
    if digit == 10:
        return 'A'

    elif digit == 11:
        return 'B'

    elif digit == 12:
        return 'C'

    elif digit == 13:
        return 'D'

    elif digit == 14:
        return 'E'

    elif digit == 15:
        return 'F'

    elif digit == 16:
        return 'G'
    else:
        return str(digit)


def subtraction(radix: int, x: str, y: str) -> str:
    answer = ''
    minus = ''
    if y == '0':
        return x

    if x.startswith('-') and y.startswith('-'):
        answer = subtraction(radix, y.replace('-', ''), x.replace('-', ''))
        return answer

    elif y.startswith('-'):
        #        answer = addition(radix,x, y.replace('-', ''))
        return answer

    elif x.startswith('-'):
        #        answer = addition(radix, x.replace('-', ''), y)
        return '-' + answer
    else:

        max_x = len(x)
        max_y = len(y)
        if max_x < max_y:
            temp_x = x
            x = y
            y = temp_x
            minus = '-'

        if max_x == max_y:
            if bigger_y_than_x(x, y):
                temp_x = x
                x = y
                y = temp_x
                minus = '-'

        c = 0
        y = y.zfill(len(x))
        i = len(x)
        while i > 0:

            digit = get_key(x[i-1]) - get_key(y[i-1]) - c

            if digit < 0:
                c = 1
                digit = radix + digit
            else:
                c = 0

            answer = get_representation(digit) + answer
            i = i-1
    return minus + answer.lstrip("0")
