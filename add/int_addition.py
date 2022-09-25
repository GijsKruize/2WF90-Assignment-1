def addition(radix, x, y):
    c = 0
    z = ''
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
        z = z + int(x[i]) + int(y[i]) + c
        if z[i] >= radix:
            z[i] = int(z[i]) - radix
            c = 1
        else:
            c = 0
    k = 0
    if c == 1:
        k = max_len + 1
        z[k - 1] = 1
    else:
        k = max_len
    z = z[::-1]
    return z[0:k]

