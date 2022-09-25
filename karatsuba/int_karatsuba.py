from multiplication.int_multiplication import multiplication
from addition.int_addition import addition
from subtraction.int_addition import subtraction

def karatsuba(radix,x,y):

    neg_x = False
    neg_y = False

    #check the first character of the string for a "-" sign
    if(x[0] == "-"):
        neg_x = True
        x = x.strip("-")
    if(y[0] == "-"):
        neg_y = True
        y = y.strip("-")

    # Multiply numbers with normal multiplication if not large enough
    if(len(x) < 2 | len(y) < 2):
        return multiplication(radix, x, y)

    # Split if numbers are large enough
    else:
        max_len = max(len(x), len(y))
        half_len = max

        # Split the numbers in a high and a low part
        x_hi = x[:-half_len]
        x_lo = x[-half_len:]
        y_hi = y[:-half_len]
        y_lo = y[-half_len:]

        # To prevent getting false splittings every hi or lo part with a length less or equal than 0 gets set to 0
        if len(x_hi) <= 0:
            x_hi = "0"
        if len(x_lo) <= 0:
            x_hi = "0"
        if len(y_lo) <= 0:
            y_lo = "0"
        if len(y_hi) <= 0:
            y_hi = "0"

        #TODO calculate the z values for further explenation see documentation 3.3.1 or lecture notes Algorithm 1.5
        z_2 = karatsuba(radix, x_hi, y_hi)
        z_0 = karatsuba(radix, x_lo, y_lo)
        z_1_prime = karatsuba(radix, addition(radix, x_hi, x_lo),addition(radix, y_hi, y_lo)) 
        z_1 = subtraction(radix, subtraction(radix, z_1_prime, z_0), z_2)

        z_prime_1 = z_2 + ((half_len * 2)*"0")
        z_prime_2 = z_1 + (half_len * "0")
        z = addition(radix, addition(radix, z_prime_1, z_prime_2), z_0)

        # if x or y was innitially negative add a - sign in front
        if(neg_x ^neg_y):
            z = "-" + z

        return z

