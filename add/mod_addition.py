
from reduction.mod_reduction import mod_reduction
from int_addition import addition
from subtraction.int_subtraction import subtraction

def mod_addition(radix,x,y,m):
    x = mod_reduction(radix, x, m)
    y = mod_reduction(radix, y, m)

    if (y == "0"):
        return x
    
    z_prime = addition(radix, x, y)[0]
    if (int(z_prime, radix) < int(m, radix)): #TODO needs to be changed to something without the double argumented int()
        return mod_reduction(radix, z_prime, m)
    
    return subtraction(radix, z_prime, m)[0]