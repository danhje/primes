'''
@author: Daniel Hjertholm
'''



import math

def is_prime(num):
    for o in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num % o == 0:
            break
    else:
        return 1

def primes(ubound):
    '''
    Starts with list of odd ints up to ubound, and uses filter to keep only
    those that are primes. Tests for primality by dividing by ints up to the
    square root of number being tested and checking if the remainder is 0.
    '''

    x = range(3, ubound, 2)
    return [2] + list(filter(is_prime, x))



if __name__ == "__main__":
    import time
    starttime = time.time()
    result = primes(10000)
    endtime = time.time()
    print(len(result), "primes found in", endtime - starttime, "seconds.")
