from subtraction.int_subtraction import subtraction


def addition(radix, x1, y1):
    negative = False
    if x1[0] == '-' and y1[0 == '-'] :
        negative = True
        x = x1[1:len(x1)]
        y = y1[1:len(y1)]
    elif x1[0] == '-':
        return subtraction(radix, y1, x1[1:len(x1)])
    elif y1[0] == '-':
        return subtraction(radix, x1, y1[1:len(y1)])
    else :
        x = x1
        y = y1

    c = 0
    z = []
    x_rev = x[::-1]
    y_rev = y[::-1]
    max_len = max(len(x), len(y))
    if len(x) - max_len > 0:
        zeroes = len(x) - max_len
        for i in range(zeroes):
            x_rev = x_rev + '0'
    elif len(y) - max_len > 0:
        zeroes = len(y) - max_len
        for i in range(zeroes):
            y_rev = y_rev + '0'
    for i in range(max_len):
        z.append(str(int(x_rev[i]) + int(y_rev[i]) + c))
        if int(z[i]) >= int(radix):
            z[i] = int(z[i]) - int(radix)
            c = 1
        else:
            c = 0
    k = 0
    if c == 1:
        k = max_len + 1
        z[k - 1] = 1
    else:
        k = max_len
    stringz = ''
    for i in z:
        stringz = stringz + str(i)
    stringz = stringz[::-1]
    if negative:
        stringz = '-' + stringz
    return stringz[0:k]
