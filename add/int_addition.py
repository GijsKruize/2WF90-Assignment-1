from subtraction.int_subtraction import *

def addition(radix,x,y):
    answer =''
    if y=='0':
        return x

    if x.startswith('-') and y.startswith('-'):
        answer = addition(radix, x.replace('-', ''), y.replace('-', ''))
        return '-' + answer

    elif x.startswith('-'):
        answer = subtraction(radix,y, x.replace('-', ''))
        return answer

    elif y.startswith('-'):
        answer = subtraction(radix, x, y.replace('-', ''))
        return answer
    else:
        supermax_33= max(len(x),len(y))
        x = x.zfill(supermax_33)
        y = y.zfill(supermax_33)

        c=0
        i=supermax_33
        while i>0:

            digit = convert_from_hex(x[i-1]) + convert_from_hex(y[i-1]) + c

            if digit >= radix:
                c = 1
                digit =  digit -radix
            else:
                c = 0

            answer = convert_to_hex(digit) + answer
            i=i-1
        if c==1:
            answer= '1' +answer
    return answer.lstrip("0")