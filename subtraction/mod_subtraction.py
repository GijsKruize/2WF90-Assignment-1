from int_subtraction import subtraction
from mod_reduce import mod_reduce


def mod_subtraction(radix,x,y,m):
    x = mod_reduce(radix, x, m)
    y = mod_reduce(radix, y, m)
    z= subtraction(radix,x,y)
    z= mod_reduce(radix, z, m)
    return(z)