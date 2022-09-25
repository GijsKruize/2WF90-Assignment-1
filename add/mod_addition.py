
from operator import mod #moet verwijderd worden als mod_reduction werkt
from int_addition import addition
from subtraction.int_subtraction import subtraction

def mod_addition(radix,x,y,m):
    #x = mod_reduction(radix, x, m)
    #y = mod_reduction(radix, y, m)
    x = mod(int(x, radix), m)
    y = mod(int(y, radix), m)

    if (y == "0"):
        return x
    
    z_prime = addition(radix, x, y)[0]
    if (int(z_prime, radix) < int(m, radix)):
        #return mod_reduction(radix, z_prime, m)
        return mod(int(z_prime, radix), m)
    
    return subtraction(radix, z_prime, m)[0]
