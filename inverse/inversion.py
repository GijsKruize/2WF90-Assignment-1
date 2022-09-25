from add.int_addition import addition
from euclidian.int_euclidian import extended_euclidian
from mod_reduce import mod_reduce

def inversion(radix,x,mod):

    g,a,y= extended_euclidian(radix,x, mod)
    if (g != 1):
        answer= "inverse does not exist"
        return answer

    else:
        a = mod_reduce(radix, a, mod)
        if a < 0:
            a=addition(radix,a,mod)
            return a

