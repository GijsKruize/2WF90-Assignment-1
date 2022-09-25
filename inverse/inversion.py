from add.int_addition import addition

def gcdExtended(a, b):
    global x, y

    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b

    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd,x,y

def inversion(x,mod,radix):

    g,x,y= gcdExtended(x, mod)
    if (g != 1):
        answer= "not possible"
        return answer

    else:
        if x < 0:


