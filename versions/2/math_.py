from operator import pow

def factorial(n):
    if isinstance(n, int) and n >= 0:
        if n:
            return n * factorial(n-1)
        return 1
    
    raise Exception("Cannot factorial a non-integer or a negative integer.")

def pow_(base, power):
    return pow(base, power)
