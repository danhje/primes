'''
@author: Daniel Hjertholm
'''



import math

def is_prime(num):
    if num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(ubound):
    '''
    Starts with list of odd ints up to ubound, and uses filter to keep only
    those that are primes. Tests for primality using the 6k +/- 1 optimization.
    '''

    x = range(3, ubound, 2)
    return [2] + list(filter(is_prime, x))



if __name__ == "__main__":
    import time
    starttime = time.time()
    result = primes(10000)
    endtime = time.time()
    print(len(result), "primes found in", endtime - starttime, "seconds.")
