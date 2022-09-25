from int_subtraction import subtraction
from mod_reduce import mod_reduce
from add.int_addition import addition


def mod_subtraction(radix,x,y,m):
    x = mod_reduce(radix, x, m)
    if x.startswith('-'):
        x=addition(radix,x,m)
    y = mod_reduce(radix, y, m)
    if y.startswith('-'):
        y=addition(radix,y,m)
    z= subtraction(radix,x,y)

    if z.startswith('-'):
        z=addition(radix,z,m)
    return(z)